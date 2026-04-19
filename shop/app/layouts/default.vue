<script setup lang="ts">

</script>

<template>
<div class="main-layout">
  <LayoutHeader class="header" />
  <main class="main">
    <slot />
  </main>
  <LayoutFooter class="footer" />
</div>
</template>

<style scoped>
.main-layout {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
.main {
  width: 1250px;
  margin: 0 auto;
  padding: 40px 0;
}
</style>