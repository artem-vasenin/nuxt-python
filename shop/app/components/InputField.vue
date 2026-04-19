<script setup lang="ts">
const data = defineModel<string>();
const { mode = 'gray' } = defineProps<{
  mode?: 'gray' | 'black';
}>();
</script>

<template>
  <input
      v-model="data"
      type="text"
      class="input"
      :class="[mode]">
</template>

<style scoped>
.input {
  width: 100%;
  border: none;
  background: transparent;
  padding: 12px 0;
  outline: none;
  color: var(--color-dark);

  &::placeholder {
    color: var(--color-gray);
  }

  &.gray {
    border-bottom: 1px solid var(--color-light-gray);
  }

  &.black {
    border-bottom: 1px solid var(--color-dark)
  }
}
</style>