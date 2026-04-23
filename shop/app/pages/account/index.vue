<script setup lang="ts">
  definePageMeta({
    middleware: 'auth',
  });

  const store = useAuthStore();
</script>

<template>
<div class="account">
  <h1>Аккаунт</h1>
  <p>
    <NuxtLink @click="store.logout" to="/auth">Выход</NuxtLink>
  </p>
</div>
</template>

<style scoped>

</style>