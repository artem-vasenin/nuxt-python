<script setup lang="ts">
import type {CategoriesResponse, ProductResponse} from "~/types/catalog.types";

const conf = useRuntimeConfig();
const select = ref('');

const { data } = await useFetch<CategoriesResponse>(conf.public.apiurl + '/categories');
const options = computed(() => (data.value?.categories || [])
    .map(c => ({ label: c.name, value: c.id })));

const { data: prods } = await useFetch<ProductResponse>(conf.public.apiurl + '/products', {
  query: { limit: 20, offset: 0 },
});
const products = prods.value?.products;
</script>

<template>
<div class="catalog">
  <h1>Каталог товаров</h1>
  <div class="content">
    <aside class="aside">
      <InputField />
      <SelectField
        v-model="select"
        :options="options"
      />
    </aside>
    <section class="products">
      <ProductCard
        v-for="(i, k) in (products || [])"
        :key="k"
        :data="i"
      />
    </section>
  </div>
</div>
</template>

<style scoped>
.catalog {
  h1 {
    padding-bottom: 40px;
  }
}
.content {
  display: grid;
  grid-template-columns: 260px 1fr;
  column-gap: 36px;
}
.aside {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.products {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 24px;
  row-gap: 70px;
}
</style>