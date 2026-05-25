<script setup>
import { ref } from 'vue'
import BaseButton from '@/components/buttons/BaseButton.vue'
const nombre = ref('Chris')
const xd = (alerta) => {
    alert(alerta)
}
</script>

<template>
    <header>
        <span>Hola, {{nombre}}</span>
    </header>
    <div>
        <BaseButton
            texto="Hola"
            color="green"
            @click="xd('Hola')"
        />

        <BaseButton
            texto="como"
            color="green"
            @click="xd('como')"
        />

        <BaseButton
            texto="estás"
            color="green"
            @click="xd('estas')"
        />
    </div>
</template>

<style scoped>
    header span{
        font-size: 32px;
        font-weight: bold;
    }
</style>