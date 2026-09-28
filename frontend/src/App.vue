<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">晶圆制造设备维护平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向晶圆厂光刻刻蚀等机台状态管理、预防性维护、报警处置与设备稼动统计的一体化设备运维后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "光刻机台", path: "/litho" }, { label: "刻蚀机台", path: "/etch" }, { label: "薄膜沉积设备", path: "/depo" }, { label: "离子注入机", path: "/implant" }, { label: "量测设备", path: "/metro" }, { label: "化学机械研磨", path: "/cmp" }, { label: "机台报警", path: "/alarm" }, { label: "预防性维护", path: "/pm" }, { label: "备件更换", path: "/sparechange" }, { label: "洁净室环境", path: "/cleanroom" }, { label: "特种气体供应", path: "/gas" }, { label: "化学品供应", path: "/chemical" }, { label: "超纯水系统", path: "/upw" }, { label: "废气处理", path: "/exhaust" }, { label: "设备点检", path: "/equipcheck" }, { label: "故障停机", path: "/downtime" }, { label: "恢复确认", path: "/recover" }, { label: "设备稼动", path: "/utilization" }]
</script>
