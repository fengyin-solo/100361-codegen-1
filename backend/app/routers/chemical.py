"""化学品供应接口：维护化学品供应点，覆盖补充化学品、登记液位偏低、停止供应等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.chemical import ChemicalService

router = APIRouter(prefix="/api/chemical", tags=["化学品供应"])

service = ChemicalService()

LIST_FIELDS = ["供应点编号", "化学品名称", "浓度规格", "储罐液位", "供应管路", "上次补充日", "责任班组", "供应状态"]
STATUSES = ["待补充", "供应正常", "液位偏低", "已停供"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按供应点编号检索"),
    status: str | None = Query(default=None, description="待补充、供应正常、液位偏低、已停供"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按供应点编号与状态过滤化学品供应列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条化学品供应点明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"化学品供应点 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条化学品供应点，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="化学品供应点已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条化学品供应点执行补充化学品、登记液位偏低、停止供应；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出化学品供应清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "chemical", "total": total, "items": items}
