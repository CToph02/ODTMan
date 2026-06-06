<script setup>
import Header from '@/components/Header.vue';
import Card from '@/components/cards/Card.vue';
</script>

<template>
    <Header/>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; width: 100%; height: 100%;">
        <Card v-for="n in 6"/>
    </div>
</template>

<style scoped>
</style>