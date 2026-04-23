<script setup lang="ts">
import type {LoginResponse} from "~/types/auth.types";

const email = ref('');
const password = ref('');
const authStore = useAuthStore();

const onSubmit = async () => {
  try {
    const data = await $fetch<LoginResponse>(useApi() + '/auth/login', {
      method: 'POST',
      body: { email: email.value, password: password.value },
    });
    authStore.loginUser(data);
    navigateTo('/catalog');
  } catch (e) {
    console.error(e);
  }
};
</script>

<template>
<div class="login">
  <h1>Мой аккаунт</h1>
  <form action="" class="form">
    <InputField
        v-model="email"
        placeholder="E-mail"
        class="form-input"
        mode="gray" />
    <InputField
        v-model="password"
        placeholder="Password"
        class="form-input"
        type="password"
        mode="gray" />
    <ActionButton
        @click.prevent="onSubmit"
        mode="primary"
        block
        class="form-btn"
    >Войти</ActionButton>
    <NuxtLink class="link" to="/auth/restore">Забыли пароль</NuxtLink>
  </form>
</div>
</template>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  align-items: center;
}
h1 {
  padding-bottom: 64px;
}
.form {
  width: 500px;
}
.form-input {
  margin-top: 46px;
}
.form-btn {
  margin-top: 70px;
}
.link {
  margin-top: 13px;
  font-weight: 400;
  font-size: 16px;
  line-height: 27px;
  letter-spacing: 0;
  text-decoration: none;
  color: var(--color-dark);
  text-align: center;
  display: inline-block;
  width: 100%;

  &:hover {
    text-decoration: underline;
  }
}
</style>