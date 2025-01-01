import { createRouter, createWebHistory } from 'vue-router';
// import App from '../App.vue';
import UpdateItem from '../components/UpdateItem.vue';

const routes = [
  // {
  //   path: '/',
  //   name: 'App',
  //   component: App
  // },
  {
    path: '/items/:id',
    name: 'ItemDetail',
    component: UpdateItem
  }
];

// Vue 3에서 라우터 인스턴스를 생성하는 방법
const router = createRouter({
  history: createWebHistory(), // createWebHistory는 기본적인 히스토리 모드
  routes
});

export default router;
