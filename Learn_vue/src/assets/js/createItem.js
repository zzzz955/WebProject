export default {
    data() {
      return {
        name: '',
        description: ''
      };
    },
    methods: {
      async createItem() {
        if (!this.name) {
          alert('아이템 이름을 입력해 주세요');
          return;
        }
  
        try {
          const response = await fetch('http://localhost:5000/items', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              name: this.name,
              description: this.description
            })
          });
  
          if (!response.ok) throw new Error('아이템 추가에 실패했습니다.');
          alert('아이템이 성공적으로 추가되었습니다.');
          this.name = '';
          this.description = '';
          location.href = '..';
        } catch (error) {
          alert(error.message);
        }
      }
    }
  };
  