<script setup lang="ts">
import type {Product, ProductResponse} from "~/types/catalog.types";

const store = useFavoriteStore();

const { data } = await useFetch<ProductResponse>(useApi() + '/products');
const list = computed<Product[]>(() => data && data.value?.total
    ? data.value.products.filter(p => store.favoriteIds.includes(p.id))
    : []);
</script>

<template>
<div class="favorites">
  <h1>Избранное</h1>
  <div class="list">
    <ProductCard v-for="i in list" :key="i.id" :data="i"/>
  </div>
</div>
</template>

<style scoped>
  .list {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    column-gap: 36px;
    row-gap: 50px;
  }
</style>