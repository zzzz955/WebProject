<template>
  <div>
    <h2>아이템 목록</h2>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} - {{ item.description }}
        <button @click="viewItem(item.id)">자세히 보기</button>
      </li>
    </ul>
  </div>
</template>

<script>
import readItemLogic from '../assets/js/readItem.js'; // 상대 경로로 import

export default {
  mixins: [readItemLogic] // updateItem.js 로직을 mixin 형태로 사용
};
</script>
