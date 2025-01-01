<template>
  <div>
    <h1>아이템 관리 시스템</h1>
    
    <CreateItem />
    <ReadItem />
    <router-view />
  </div>
</template>

<script>
import CreateItem from './components/CreateItem.vue'
import ReadItem from './components/ReadItem.vue'

export default {
  components: {
    CreateItem,
    ReadItem
  }
}
</script>
