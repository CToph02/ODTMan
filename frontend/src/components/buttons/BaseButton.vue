<script setup>
defineProps({
  texto: {
    type: String,
    default: 'Aceptar'
  },
  color: {
    type: String,
    default: 'white'
  },
  type: {
    type: String,
    default: 'button'
  }
})

defineEmits(['click'])
</script>

<template>
  <button 
    :class="['btn-generico', `btn-${color}`]" 
    @click="$emit('click')"
  >
    {{ texto }}
  </button>
</template>

<style scoped>
.btn-generico {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.btn-blue { background-color: #3490dc; color: white; }
.btn-green { background-color: #38c172; color: white; }
.btn-red { background-color: #e3342f; color: white; }
</style>