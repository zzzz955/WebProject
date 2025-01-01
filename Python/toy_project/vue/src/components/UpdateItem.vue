<template>
  <div v-if="item">
    <h2>아이템 수정</h2>
    <div>
      <label>아이템 이름:</label>
      <input v-model="item.name" />
    </div>
    <div>
      <label>아이템 설명:</label>
      <input v-model="item.description" />
    </div>
    <button @click="updateItem">수정 완료</button>
    <button @click="deleteItem">삭제</button>
    <button @click="goBack">취소</button>
  </div>
  <div v-else>
    <p>아이템을 불러오는 중...</p>
  </div>
</template>

<script>
import updateItemLogic from '../assets/js/updateItem.js'; // 상대 경로로 import

export default {
  mixins: [updateItemLogic] // updateItem.js 로직을 mixin 형태로 사용
};
</script>
