<script setup lang="ts">

</script>

<template>
<footer class="layout-footer">
    <div class="top">
      <nav class="navFooter">
        <ul class="navFooter_list">
          <li class="navFooter_item">
            <NuxtLink>Контакты</NuxtLink>
          </li>
          <li class="navFooter_item">
            <NuxtLink>Условия покупки</NuxtLink>
          </li>
          <li class="navFooter_item">
            <NuxtLink>Доставка и возврат</NuxtLink>
          </li>
        </ul>
      </nav>
    <InputField
        mode="black"
        class="footerInput"
        placeholder="Ваш email для акций и предложений"/>
    </div>
    <div class="bottom">
      <div class="copy">&copy; 2024 Shoppe</div>
      <div class="icons">
        <NuxtLink to="https://linkedin.com">
          <IconIn/>
        </NuxtLink>
        <NuxtLink to="https://fb.com">
          <IconFb/>
        </NuxtLink>
        <NuxtLink>
          <IconInsta/>
        </NuxtLink>
        <NuxtLink to="https://twiter.com">
          <IconTwitter />
        </NuxtLink>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.layout-footer {
  width: 1250px;
  margin: 0 auto;
  padding: 40px 0;
  border-top: 1px solid var(--color-light-gray);
}
.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.navFooter {
  flex: 1;
  padding-bottom: 46px;
}
.navFooter_list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 30px;
}
.navFooter_item {
  font-weight: 400;
  font-size: 16px;
  line-height: 27px;
  text-transform: uppercase;
}
.footerInput {
  flex: 0 0 400px;
  max-width: 400px;
  margin-bottom: 46px;
}
.bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.copy {
  flex: 1;
  color: var(--color-dark);
}
.icons {
  flex: 0 0 400px;
  max-width: 400px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 30px;
}
</style>