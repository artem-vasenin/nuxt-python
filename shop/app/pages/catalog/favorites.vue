<script setup lang="ts">
const store = useFavoriteStore();

store.addToFavorite(3);
console.log(store.favoriteIds);
await callOnce('fetchCat', () => store.tmpFetchData(), { mode: 'navigation' });
</script>

<template>
<div class="favorites">
  <h1>Избранное</h1>
  <div class="list">
<!--    <ProductCard-->
<!--        v-for="(i, k) in store.favoriteIds || []"-->
<!--        :key="i"-->
<!--        :data="i"-->
<!--      />-->
    {{store.favoriteIds[0]}}
  </div>
</div>
</template>

<style scoped>

</style>