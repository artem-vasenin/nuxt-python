<script setup lang="ts">
import type {CategoriesResponse, ProductResponse} from "~/types/catalog.types";

const conf = useRuntimeConfig();
const route = useRoute();
const router = useRouter();
const category_id = ref(route.query.category_id ?? '');
const search = ref(route.query.search || '');

const { data } = await useFetch<CategoriesResponse>(conf.public.apiurl + '/categories');
const options = computed(() => (data.value?.categories || [])
    .map(c => ({ label: c.name, value: c.id })));

const query = computed(() => ({
      limit: route.query.limit || 20,
      offset: route.query.offset || 0,
      category_id: route.query.category_id || undefined,
      search: route.query.search || undefined,
}));

const { data: prods } = await useFetch<ProductResponse>(conf.public.apiurl + '/products', {
  query,
});

watchEffect(() => {
  router.replace({ query: { category_id: category_id.value, search: search.value } });
});
</script>

<template>
<div class="catalog">
  <h1>Каталог товаров</h1>
  <div class="content">
    <aside class="aside">
      <InputField v-model="search" placeholder="Search" />
      <SelectField
        v-model="category_id"
        :options="[{label: 'Категории', value: ''}, ...options]"
      />
    </aside>
    <section class="products">
      <ProductCard
        v-for="(i, k) in prods?.products || []"
        :key="i.id"
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