<script setup>
import { RouterView } from 'vue-router';
</script>

<template>
  <RouterView />
</template>

<style>
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: sans-serif; /* Opcional: Un tipo de letra limpio para empezar */
  background-color: #f4f6f9; /* Opcional: Un fondo gris claro común en paneles */
  min-height: 100vh;
  width: 100%;
}
</style>