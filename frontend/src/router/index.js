import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue' 
import Cadastro from '../views/PessoaView.vue' 

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cadastro',  // A URL que deve levar à tela de cadastro
    name: 'Cadastro',
    component: Cadastro
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
