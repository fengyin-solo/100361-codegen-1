"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import litho as router_litho
from app.routers import etch as router_etch
from app.routers import depo as router_depo
from app.routers import implant as router_implant
from app.routers import metro as router_metro
from app.routers import cmp as router_cmp
from app.routers import alarm as router_alarm
from app.routers import pm as router_pm
from app.routers import sparechange as router_sparechange
from app.routers import cleanroom as router_cleanroom
from app.routers import gas as router_gas
from app.routers import chemical as router_chemical
from app.routers import upw as router_upw
from app.routers import exhaust as router_exhaust
from app.routers import equipcheck as router_equipcheck
from app.routers import downtime as router_downtime
from app.routers import recover as router_recover
from app.routers import utilization as router_utilization

ROUTERS = [router_litho, router_etch, router_depo, router_implant, router_metro, router_cmp, router_alarm, router_pm, router_sparechange, router_cleanroom, router_gas, router_chemical, router_upw, router_exhaust, router_equipcheck, router_downtime, router_recover, router_utilization]
