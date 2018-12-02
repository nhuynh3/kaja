import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Collection from './views/Collection.vue'
import Add from './views/Add.vue'
import Portfolio from './views/Portfolio.vue'

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/collection',
      name: 'collection',
      component: Collection
    },
    {
      path: '/add',
      name: 'add',
      component: Add
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      component: Portfolio
    }
  ]
})
