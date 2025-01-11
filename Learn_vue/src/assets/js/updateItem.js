export default {
    data() {
      return {
        item: null
      };
    },
    mounted() {
      this.fetchItem();
    },
    methods: {
      async fetchItem() {
        const response = await fetch(`http://localhost:5000/items/${this.$route.params.id}`);
        const data = await response.json();
        this.item = data;
      },
      async updateItem() {
        if (!this.item.name) {
          alert('아이템 이름을 입력해 주세요');
          return;
        }
  
        try {
          const response = await fetch(`http://localhost:5000/items/${this.item.id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.item)
          });
  
          if (!response.ok) throw new Error('아이템 수정에 실패했습니다.');
          alert('아이템이 수정되었습니다.');
          this.goBack();
        } catch (error) {
          alert(error.message);
        }
      },
      async deleteItem() {
        try {
          const response = await fetch(`http://localhost:5000/items/${this.item.id}`, {
            method: 'DELETE'
          });
  
          if (!response.ok) throw new Error('아이템 삭제에 실패했습니다.');
          alert('아이템이 삭제되었습니다.');
          this.goBack();
        } catch (error) {
          alert(error.message);
        }
      },
      goBack() {
        location.href = '..';
      }
    }
  };
  