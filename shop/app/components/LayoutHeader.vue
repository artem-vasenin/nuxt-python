<script setup lang="ts">

</script>

<template>
<header class="layout-header">
  <div class="logo">
    <NuxtLink to="/">
      <span class="logo_first">S</span>
      <span class="logo_rest">HOPPE</span>
    </NuxtLink>
  </div>
  <nav class="nav">
    <ul class="menu">
      <li class="menu_item">
        <NuxtLink to="/catalog">Магазин</NuxtLink>
      </li>
      <li class="menu_item">
        <NuxtLink to="/about">О нас</NuxtLink>
      </li>
    </ul>
  </nav>
  <ul class="icons">
    <li class="icons_item">
      <NuxtLink to="/"><IconSearch/></NuxtLink>
    </li>
    <li class="icons_item">
      <NuxtLink to="/cart"><IconCart/></NuxtLink>
    </li>
    <li class="icons_item">
      <NuxtLink to="/catalog/favorites"><IconHeart/></NuxtLink>
    </li>
    <li class="icons_item">
      <NuxtLink to="/account"><IconUser/></NuxtLink>
    </li>
  </ul>
</header>
</template>

<style scoped>
.layout-header {
  width: 1250px;
  margin: 0 auto;
  padding: 40px 0 16px;
  border-bottom: 1px solid var(--color-light-gray);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo {
  font-family: var(--font-as), sans-serif;

  a {
    text-decoration: none;
  }
}
.logo_first, .logo_rest {
  font-weight: 400;
  font-size: 35px;
  line-height: 1;
  letter-spacing: 0;
  color: var(--color-dark);
}
.logo_first {
  color: var(--color-brown);
}

.nav {
  flex: 1;
  text-align: right;

  &::after {
    content: '|';
  }
}
.menu {
  margin: 0;
  padding: 0 60px 0 0;
  list-style: none;
  display: inline-flex;
  align-items: center;
  gap: 60px;
}
.menu_item a {
  font-weight: 400;
  font-size: 16px;
  line-height: 1;
  letter-spacing: 0;
  text-decoration: none;
  color: var(--color-gray);

  &.router-link-exact-active {
    color: var(--color-dark);
  }
}
.icons {
  margin: 0;
  padding: 0 0 0 60px;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 40px;

  a {
    position: relative;
    &.router-link-exact-active {
      &::after {
        content: '';
        display: block;
        width: 100%;
        height: 2px;
        background: var(--color-dark);
        position: absolute;
        left: 0;
        bottom: -25px;
      }
    }
  }
}
</style>