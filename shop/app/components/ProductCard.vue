<script setup lang="ts">
import type {Product} from "~/types/catalog.types";

const props = defineProps<{ data: Product }>();
const conf = useRuntimeConfig();
</script>

<template>
  <div class="wrap" @click="navigateTo('/catalog/' + props.data.id)">
    <div class="top">
      <span class="favorite">
        <IconHeartFilled/>
      </span>
      <span v-if="props.data.discount" class="discount">-{{props.data.discount}}%</span>
    </div>
    <div class="center">
      <img v-if="props.data.images" :src="`${conf.public.imgurl}${props.data.images[0]}`" alt="img" class="img">
    </div>
    <div class="bottom">
      <div class="name">{{props.data.name}}</div>
      <div class="price">$ {{props.data.price}},00</div>
    </div>
  </div>
</template>

<style scoped>
.wrap {
  position: relative;
  cursor: pointer;

  &:hover {
    .img {
      box-shadow: 0 0 18px rgb(0 0 0 / .3);
      transition: box-shadow .3s;
    }
  }
}
.top {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
  position: absolute;
  top: 16px;
  left: 16px;
  right: 16px;
  z-index: 1;
}
.discount {
  font-weight: 400;
  font-size: 12px;
  line-height: 20px;
  letter-spacing: 0;
  color: white;
  display: inline-block;
  min-height: 24px;
  background-color: #A18A68;
  border-radius: 4px;
  padding: 2px 8px;
}
.favorite {
  font-size: 20px;
}
.img {
  max-width: 300px;
  border-radius: 8px;
      transition: box-shadow .3s;
}
.name {
  font-weight: 400;
  font-size: 20px;
  line-height: 26px;
  color: var(--color-dark);
  padding-top: 24px;
}
.price {
  font-weight: 500;
  font-size: 20px;
  line-height: 26px;
  text-transform: capitalize;
  color: var(--color-brown);
  padding-top: 16px;
}
</style>