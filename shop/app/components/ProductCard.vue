<script setup lang="ts">
import type {Product} from "~/types/catalog.types";

const { data } = defineProps<{ data: Product }>();
const conf = useRuntimeConfig();
const storeFavorite = useFavoriteStore();
const isFavorite = computed(() => storeFavorite.favoriteIds.includes(data.id));

const updateFavorite = (event: MouseEvent) => {
  event.stopPropagation();

  if (isFavorite.value) {
    storeFavorite.delFavorite(data.id);
  } else {
    storeFavorite.addToFavorite(data.id);
  }
};

// const handleWrapClick = (event: MouseEvent) => {
//   const target = event.target as HTMLElement;
//   const isButton = target.closest('button');
//
//   if (!isButton) {
//     navigateTo('/catalog/' + data.id);
//   }
// };
</script>

<template>
  <div class="wrap" @click="navigateTo('/catalog/' + data.id)">
    <div class="top">
      <button
          @click.stop="updateFavorite"
          :class="['favorite', {isFavorite}]"
      ><IconHeartFilled/></button>
      <span class="discount" v-if="data.discount">-{{data.discount}}%</span>
    </div>
    <div class="center">
      <img v-if="data.images" :src="`${conf.public.imgurl}${data.images[0]}`" alt="img" class="img">
    </div>
    <div class="bottom">
      <div class="name">{{data.name}}</div>
      <div class="price">$ {{data.price}},00</div>
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

    .favorite {
      opacity: 1;
      pointer-events: initial;
      transition: opacity .3s;
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
  border: none;
  background-color: transparent;
  padding: 0;
  margin: 0;
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s;

  &.isFavorite {
    opacity: 1;
    pointer-events: initial;
    transition: opacity .3s;
  }
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