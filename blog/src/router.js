import { createRouter, createWebHistory } from 'vue-router'
// import Home from './components/Home.vue'
// import About from './components/About.vue'
import Blog  from './components/Blog.vue'
import Task from './components/Task.vue'
import Form from './components/Form.vue'
import About from './components/About.vue'

const routes = [
  { path: '/', component: Blog },
  { path: '/form', component: Form },
  { path: '/task', component: Task },
  {path: '/about', component: About},
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
