import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Litho = () => import('@/views/litho/index.vue')
const Etch = () => import('@/views/etch/index.vue')
const Depo = () => import('@/views/depo/index.vue')
const Implant = () => import('@/views/implant/index.vue')
const Metro = () => import('@/views/metro/index.vue')
const Cmp = () => import('@/views/cmp/index.vue')
const Alarm = () => import('@/views/alarm/index.vue')
const Pm = () => import('@/views/pm/index.vue')
const Sparechange = () => import('@/views/sparechange/index.vue')
const Cleanroom = () => import('@/views/cleanroom/index.vue')
const Gas = () => import('@/views/gas/index.vue')
const Chemical = () => import('@/views/chemical/index.vue')
const Upw = () => import('@/views/upw/index.vue')
const Exhaust = () => import('@/views/exhaust/index.vue')
const Equipcheck = () => import('@/views/equipcheck/index.vue')
const Downtime = () => import('@/views/downtime/index.vue')
const Recover = () => import('@/views/recover/index.vue')
const Utilization = () => import('@/views/utilization/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/litho', name: 'litho', component: Litho },
    { path: '/etch', name: 'etch', component: Etch },
    { path: '/depo', name: 'depo', component: Depo },
    { path: '/implant', name: 'implant', component: Implant },
    { path: '/metro', name: 'metro', component: Metro },
    { path: '/cmp', name: 'cmp', component: Cmp },
    { path: '/alarm', name: 'alarm', component: Alarm },
    { path: '/pm', name: 'pm', component: Pm },
    { path: '/sparechange', name: 'sparechange', component: Sparechange },
    { path: '/cleanroom', name: 'cleanroom', component: Cleanroom },
    { path: '/gas', name: 'gas', component: Gas },
    { path: '/chemical', name: 'chemical', component: Chemical },
    { path: '/upw', name: 'upw', component: Upw },
    { path: '/exhaust', name: 'exhaust', component: Exhaust },
    { path: '/equipcheck', name: 'equipcheck', component: Equipcheck },
    { path: '/downtime', name: 'downtime', component: Downtime },
    { path: '/recover', name: 'recover', component: Recover },
    { path: '/utilization', name: 'utilization', component: Utilization },
  ],
})

export default router
