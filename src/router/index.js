import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Predictions from '../views/Predictions.vue'
import WhaleWatch from '../views/WhaleWatch.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }, 
  {
    path: '/whalewatch',
    name: 'WhaleWatch',
    component: WhaleWatch
  },
  {
    path: '/predictions',
    name: 'Predictions',
    component: Predictions
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
