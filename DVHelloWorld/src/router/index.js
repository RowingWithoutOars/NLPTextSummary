import Vue from 'vue'
import Router from 'vue-router'
import RToP from '@/components/RecordTextofPolice'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'RToP',
      component: RToP
    }
  ]
})
