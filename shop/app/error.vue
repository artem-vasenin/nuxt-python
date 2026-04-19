<script setup lang="ts">
import type {NuxtError} from "#app";

const { error } = defineProps<{ error: NuxtError }>();
const text404 = 'Страница не найдена, попробуйте перейти на главную страницу';

const goToHome = () => navigateTo('/');
</script>

<template>
  <NuxtLayout>
    <div class="error">
      <h1>{{error.status}} ошибка</h1>
      <p>{{error.status === 404 ? text404 : error.statusText}}</p>
      <ActionButton
          mode="outline"
          @click="goToHome"
          className="btn"
      >Главная страница</ActionButton>
    </div>
  </NuxtLayout>
</template>

<style scoped>
.error {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  h1 {
    margin: 0;
    padding-bottom: 24px;
  }

  .btn {
    margin-top: 64px;
  }
}
</style>