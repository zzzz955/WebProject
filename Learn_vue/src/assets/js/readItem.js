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