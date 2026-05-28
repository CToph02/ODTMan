import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import Header from '@/components/Header.vue'

const routes = [
  {path: '/', component: LoginView},
  {path: '/home', component: Header}
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router;