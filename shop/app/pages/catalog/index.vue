<script setup lang="ts">
import type {CategoriesResponse} from "~/types/catalog.types";

const conf = useRuntimeConfig();
const select = ref('');

const { data } = await useFetch<CategoriesResponse>(conf.public.apiurl + '/categories');
const options = computed(() => (data.value?.categories || [])
    .map(c => ({ label: c.name, value: c.id })));
</script>

<template>
<div class="catalog">
  <h1>Каталог товаров</h1>
  <div class="content">
    <aside class="aside">
      <InputField />
      <SelectField
        v-model="select"
        :options="[{ label: 'Категории', value: '' }, ...options]"
      />
    </aside>
    <section class="products">
      Products
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
</style>