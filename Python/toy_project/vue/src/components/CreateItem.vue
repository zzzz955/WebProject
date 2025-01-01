<template>
  <div>
    <h2>아이템 추가</h2>
    <input v-model="name" placeholder="아이템 이름" />
    <input v-model="description" placeholder="아이템 설명" />
    <button @click="createItem">아이템 추가</button>
  </div>
</template>

<script>
import createItemLogic from '../assets/js/createItem.js'; // 상대 경로로 import

export default {
  mixins: [createItemLogic] // createItem.js 로직을 mixin 형태로 사용
};
</script>
