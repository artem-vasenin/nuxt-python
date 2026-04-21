<script setup lang="ts">
interface Option {
  label: string;
  value: string | number;
  disabled?: boolean;
  selected?: boolean;
}

const model = defineModel<string | number>();

const props = defineProps<{
  options: Option[];
}>()
</script>

<template>
  <select
      v-model="model"
      name="select"
      class="select">
    <option
        v-for="(i, k) in props.options"
        :key="k"
        :value="i.value"
        :disabled="!!i.disabled"
        :selected="!!i.selected"
    >{{i.label}}</option>
  </select>
</template>

<style scoped>
.select {
  height: 53px;
  width: 100%;
  border: 1px solid #D8D8D8;
  border-radius: 4px;
  padding: 12px;
  outline: none;
}
</style>