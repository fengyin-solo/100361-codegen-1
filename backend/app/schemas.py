"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class LithoEntry(BaseModel):
    """光刻机台明细结构。"""

    field_0: str | None = None  # 机台编号
    field_1: str | None = None  # 机台型号
    field_2: str | None = None  # 曝光波长
    field_3: str | None = None  # 日产片数
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次保养日
    field_6: str | None = None  # 稼动率
    field_7: str | None = None  # 机台状态

class EtchEntry(BaseModel):
    """刻蚀机台明细结构。"""

    field_0: str | None = None  # 机台编号
    field_1: str | None = None  # 刻蚀方式
    field_2: str | None = None  # 腔体数量
    field_3: str | None = None  # 工艺配方
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次清洗日
    field_6: str | None = None  # 颗粒数
    field_7: str | None = None  # 机台状态

class DepoEntry(BaseModel):
    """薄膜沉积设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 沉积方式
    field_2: str | None = None  # 膜厚目标值
    field_3: str | None = None  # 靶材寿命
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次换靶日
    field_6: str | None = None  # 膜厚偏差
    field_7: str | None = None  # 设备状态

class ImplantEntry(BaseModel):
    """离子注入机明细结构。"""

    field_0: str | None = None  # 机台编号
    field_1: str | None = None  # 注入元素
    field_2: str | None = None  # 注入能量
    field_3: str | None = None  # 束流强度
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次调束日
    field_6: str | None = None  # 束流偏差
    field_7: str | None = None  # 机台状态

class MetroEntry(BaseModel):
    """量测设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 量测项目
    field_2: str | None = None  # 量程范围
    field_3: str | None = None  # 校准周期
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次校准日
    field_6: str | None = None  # 量测偏差
    field_7: str | None = None  # 设备状态

class CmpEntry(BaseModel):
    """研磨设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 研磨垫寿命
    field_2: str | None = None  # 研磨液批次
    field_3: str | None = None  # 去除速率
    field_4: str | None = None  # 所属厂房
    field_5: str | None = None  # 上次换垫日
    field_6: str | None = None  # 划伤片数
    field_7: str | None = None  # 设备状态

class AlarmEntry(BaseModel):
    """机台报警单明细结构。"""

    field_0: str | None = None  # 报警编号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 报警代码
    field_3: str | None = None  # 报警级别
    field_4: str | None = None  # 触发时间
    field_5: str | None = None  # 处理人
    field_6: str | None = None  # 恢复时间
    field_7: str | None = None  # 报警状态

class PmEntry(BaseModel):
    """预防性维护单明细结构。"""

    field_0: str | None = None  # 保养单号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 保养项目
    field_3: str | None = None  # 计划开始日
    field_4: str | None = None  # 计划工时
    field_5: str | None = None  # 执行班组
    field_6: str | None = None  # 执行人
    field_7: str | None = None  # 保养状态

class SparechangeEntry(BaseModel):
    """备件更换单明细结构。"""

    field_0: str | None = None  # 更换单号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 备件名称
    field_3: str | None = None  # 备件批次
    field_4: str | None = None  # 更换数量
    field_5: str | None = None  # 更换日期
    field_6: str | None = None  # 更换人
    field_7: str | None = None  # 更换状态

class CleanroomEntry(BaseModel):
    """洁净室区域明细结构。"""

    field_0: str | None = None  # 区域编号
    field_1: str | None = None  # 洁净等级
    field_2: str | None = None  # 温度设定
    field_3: str | None = None  # 湿度设定
    field_4: str | None = None  # 悬浮粒子数
    field_5: str | None = None  # 压差值
    field_6: str | None = None  # 检测日期
    field_7: str | None = None  # 区域状态

class GasEntry(BaseModel):
    """特气气源明细结构。"""

    field_0: str | None = None  # 气源编号
    field_1: str | None = None  # 气体种类
    field_2: str | None = None  # 纯度等级
    field_3: str | None = None  # 钢瓶数量
    field_4: str | None = None  # 供气压力
    field_5: str | None = None  # 更换日期
    field_6: str | None = None  # 责任班组
    field_7: str | None = None  # 气源状态

class ChemicalEntry(BaseModel):
    """化学品供应点明细结构。"""

    field_0: str | None = None  # 供应点编号
    field_1: str | None = None  # 化学品名称
    field_2: str | None = None  # 浓度规格
    field_3: str | None = None  # 储罐液位
    field_4: str | None = None  # 供应管路
    field_5: str | None = None  # 上次补充日
    field_6: str | None = None  # 责任班组
    field_7: str | None = None  # 供应状态

class UpwEntry(BaseModel):
    """超纯水系统明细结构。"""

    field_0: str | None = None  # 系统编号
    field_1: str | None = None  # 产水电阻率
    field_2: str | None = None  # 产水流量
    field_3: str | None = None  # 回收率
    field_4: str | None = None  # 供水压力
    field_5: str | None = None  # 上次换膜日
    field_6: str | None = None  # 在线监测值
    field_7: str | None = None  # 系统状态

class ExhaustEntry(BaseModel):
    """废气处理装置明细结构。"""

    field_0: str | None = None  # 装置编号
    field_1: str | None = None  # 处理方式
    field_2: str | None = None  # 处理风量
    field_3: str | None = None  # 去除效率
    field_4: str | None = None  # 排放浓度
    field_5: str | None = None  # 上次换药日
    field_6: str | None = None  # 责任班组
    field_7: str | None = None  # 装置状态

class EquipcheckEntry(BaseModel):
    """设备点检单明细结构。"""

    field_0: str | None = None  # 点检单号
    field_1: str | None = None  # 点检部位
    field_2: str | None = None  # 点检项目
    field_3: str | None = None  # 点检标准
    field_4: str | None = None  # 实测值
    field_5: str | None = None  # 点检人
    field_6: str | None = None  # 点检日期
    field_7: str | None = None  # 点检状态

class DowntimeEntry(BaseModel):
    """故障停机记录明细结构。"""

    field_0: str | None = None  # 停机编号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 故障现象
    field_3: str | None = None  # 停机开始时间
    field_4: str | None = None  # 停机时长
    field_5: str | None = None  # 责任工程师
    field_6: str | None = None  # 恢复时间
    field_7: str | None = None  # 停机状态

class RecoverEntry(BaseModel):
    """恢复确认单明细结构。"""

    field_0: str | None = None  # 确认单号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 首片结果
    field_3: str | None = None  # 连续合格片数
    field_4: str | None = None  # 确认工程师
    field_5: str | None = None  # 确认日期
    field_6: str | None = None  # 放行结论
    field_7: str | None = None  # 确认状态

class UtilizationEntry(BaseModel):
    """设备稼动记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 关联机台
    field_2: str | None = None  # 统计周期
    field_3: str | None = None  # 计划稼动时长
    field_4: str | None = None  # 实际稼动时长
    field_5: str | None = None  # 停机时长
    field_6: str | None = None  # 稼动率
    field_7: str | None = None  # 记录状态
