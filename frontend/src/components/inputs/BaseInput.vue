<script setup>
defineProps({
    ph_input:{
        type: String,
        default: " "
    }
})
</script>

<template>
    <input type="text" :placeholder="ph_input">

</template>

<style scoped>
</style>