<script setup lang="ts">
const route = useRoute();
const id = ref(route.params.id);
</script>

<template>
<div class="product">Product {{id}}</div>
</template>

<style scoped>

</style>