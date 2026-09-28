<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "光刻机台", "created": 0, "pending": 0, "abnormal": 0}, {"name": "刻蚀机台", "created": 0, "pending": 0, "abnormal": 0}, {"name": "薄膜沉积设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "离子注入机", "created": 0, "pending": 0, "abnormal": 0}, {"name": "量测设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "化学机械研磨", "created": 0, "pending": 0, "abnormal": 0}, {"name": "机台报警", "created": 0, "pending": 0, "abnormal": 0}, {"name": "预防性维护", "created": 0, "pending": 0, "abnormal": 0}, {"name": "备件更换", "created": 0, "pending": 0, "abnormal": 0}, {"name": "洁净室环境", "created": 0, "pending": 0, "abnormal": 0}, {"name": "特种气体供应", "created": 0, "pending": 0, "abnormal": 0}, {"name": "化学品供应", "created": 0, "pending": 0, "abnormal": 0}, {"name": "超纯水系统", "created": 0, "pending": 0, "abnormal": 0}, {"name": "废气处理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "设备点检", "created": 0, "pending": 0, "abnormal": 0}, {"name": "故障停机", "created": 0, "pending": 0, "abnormal": 0}, {"name": "恢复确认", "created": 0, "pending": 0, "abnormal": 0}, {"name": "设备稼动", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
