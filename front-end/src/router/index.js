import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../SFC/MainPage.vue'
import Veritabanı from '../SFC/Veritabanı.vue'
import Günlüğüm from '../SFC/Günlüğüm.vue'
import İletişim from '../SFC/İletişim.vue'
import SpesificBook from '../SFC/SpesificBook.vue'

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/Kaynaklar',
    name: 'Veritabanı',
    component: Veritabanı
  },
  {
    path: '/Gunlugum',
    name: 'Günlüğüm',
    component: Günlüğüm
  },
  {
    path: '/:name',
    name: 'SpesificBook', 
    component: SpesificBook
  },
  {
    path: '/Mesaj',
    name: 'İletişim',
    component: İletişim
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
