# 晶圆制造设备维护平台

面向晶圆厂光刻刻蚀等机台状态管理、预防性维护、报警处置与设备稼动统计的一体化设备运维后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 光刻机台 | `litho` | 光刻机台 | 机台编号、机台型号、曝光波长 |
| 刻蚀机台 | `etch` | 刻蚀机台 | 机台编号、刻蚀方式、腔体数量 |
| 薄膜沉积设备 | `depo` | 薄膜沉积设备 | 设备编号、沉积方式、膜厚目标值 |
| 离子注入机 | `implant` | 离子注入机 | 机台编号、注入元素、注入能量 |
| 量测设备 | `metro` | 量测设备 | 设备编号、量测项目、量程范围 |
| 化学机械研磨 | `cmp` | 研磨设备 | 设备编号、研磨垫寿命、研磨液批次 |
| 机台报警 | `alarm` | 机台报警单 | 报警编号、关联机台、报警代码 |
| 预防性维护 | `pm` | 预防性维护单 | 保养单号、关联机台、保养项目 |
| 备件更换 | `sparechange` | 备件更换单 | 更换单号、关联机台、备件名称 |
| 洁净室环境 | `cleanroom` | 洁净室区域 | 区域编号、洁净等级、温度设定 |
| 特种气体供应 | `gas` | 特气气源 | 气源编号、气体种类、纯度等级 |
| 化学品供应 | `chemical` | 化学品供应点 | 供应点编号、化学品名称、浓度规格 |
| 超纯水系统 | `upw` | 超纯水系统 | 系统编号、产水电阻率、产水流量 |
| 废气处理 | `exhaust` | 废气处理装置 | 装置编号、处理方式、处理风量 |
| 设备点检 | `equipcheck` | 设备点检单 | 点检单号、点检部位、点检项目 |
| 故障停机 | `downtime` | 故障停机记录 | 停机编号、关联机台、故障现象 |
| 恢复确认 | `recover` | 恢复确认单 | 确认单号、关联机台、首片结果 |
| 设备稼动 | `utilization` | 设备稼动记录 | 记录编号、关联机台、统计周期 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
