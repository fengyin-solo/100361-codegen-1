"""洁净室环境接口：维护洁净室区域，覆盖提交检测、标记超标、隔离区域等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.cleanroom import CleanroomService

router = APIRouter(prefix="/api/cleanroom", tags=["洁净室环境"])

service = CleanroomService()

LIST_FIELDS = ["区域编号", "洁净等级", "温度设定", "湿度设定", "悬浮粒子数", "压差值", "检测日期", "区域状态"]
STATUSES = ["待检测", "环境达标", "环境超标", "已隔离"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按区域编号检索"),
    status: str | None = Query(default=None, description="待检测、环境达标、环境超标、已隔离"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按区域编号与状态过滤洁净室环境列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条洁净室区域明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"洁净室区域 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条洁净室区域，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="洁净室区域已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条洁净室区域执行提交检测、标记超标、隔离区域；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出洁净室环境清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "cleanroom", "total": total, "items": items}
