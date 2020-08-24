import Vue from 'vue'
import Router from 'vue-router'
// import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login/',
      name: 'Login',
      component: () => import('../components/Login')
    },
    {
      path: '/register/',
      name: 'Register',
      component: () => import('../components/Register')
    },
    {
      path: '/',
      name: 'AtmsIndex',
      component: () => import('../components/AtmsIndex'),
      // component: () => import('../components/ShowLog'),
      children: [
        {
          path: '/show_testcases/',
          name: 'TestCaseList',
          component: () => import('../components/TestCaseList'),
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/index/',
          name: 'Home',
          component: () => import('../components/Home')
        },
        {
          path: '/execute_testcase/',
          name: 'ExecutePage',
          component: () => import('../components/ExecutePage')
        },
        {
          path: '/show_pathtree',
          name: 'ShowPathTree',
          component: () => import('../components/ShowPathTree')
        }
      ]
    }
  ]
})
