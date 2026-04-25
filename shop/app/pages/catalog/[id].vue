<script setup lang="ts">
import type {Product} from "~/types/catalog.types";

const route = useRoute();
const id = ref(route.params.id);
const { data } = await useFetch<{product: Product}>(`${useApi()}/products/${id.value}`);

console.log(data.value);

useSeoMeta({
  title: (data.value?.product?.name || id).toString(),
})
</script>

<template>
<div class="product">Product {{id}}</div>
</template>

<style scoped>

</style>