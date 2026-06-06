import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import HomeView from '@/views/HomeView.vue'

const routes = [
  {path: '/', component: LoginView},
  { 
    path: '/home', 
    component: HomeView,
    meta: { requiresAuth: true } 
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) =>{
  const isAuthenticated = localStorage.getItem('access');
  if (to.meta.requiresAuth && !isAuthenticated){
    next('/')
  }else if (to.path === '/' && isAuthenticated){
    next('/home')
  }else{
    next()
  }
})

export default router;