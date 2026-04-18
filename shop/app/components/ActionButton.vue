<script setup lang="ts">
const { mode = 'primary', block = false, className } = defineProps<{
  mode?: 'primary' | 'outline';
  block?: boolean;
  className?: string;
}>();
</script>

<template>
  <button
      class="button"
      :class="[ mode, className, { block }]"
  >
    <slot/>
  </button>
</template>

<style scoped>
.button {
  border: 1px solid var(--color-dark);
  border-radius: 4px;
  font-weight: 700;
  line-height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 53px;
  padding: 10px 30px;
  font-size: 16px;
  cursor: pointer;

  &.primary {
    background: var(--color-dark);
    color: white;
  }

  &.outline {
    background: transparent;
    color: var(--color-dark)
  }

  &.block {
    width: 100%;
  }

  &:hover {
    opacity: .7;
  }
}
</style>