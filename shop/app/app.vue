<script setup lang="ts">
import '~/assets/styles/main.css';
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<style scoped>
.page-enter-active, .page-leave-active {
  transition: opacity .5s;
}
.page-enter-from, .page-leave-to {
  opacity: 0;
}
</style>