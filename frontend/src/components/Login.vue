<script setup>
import BaseButton from './buttons/BaseButton.vue';
</script>

<template>
    
    <div class="btn-auth">
        <BaseButton
            texto="Iniciar sesión"
            color="blue"
        />
        <BaseButton
            texto="Registrarse"
            color="red"
        />
    </div>
    
</template>

<style scoped>
.btn-auth{
    display: flex;
    gap: 8px;
}
</style>