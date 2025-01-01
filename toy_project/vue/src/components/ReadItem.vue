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
export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    this.fetchItems();
  },
  methods: {
    async fetchItems() {
      const response = await fetch('http://localhost:5000/items');
      const data = await response.json();
      this.items = data;
    },
    viewItem(id) {
      this.$router.push({ name: 'ItemDetail', params: { id: id } });
    }
  }
};
</script>
