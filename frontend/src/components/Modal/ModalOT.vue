<script setup>
import BaseButton from '../buttons/BaseButton.vue';
const props = defineProps({
    order:{
        type: Object,
        default: null
    }
})
</script>

<template>
    <div class="modal-ot">
        <p>Hola</p>
        <p style="font-size: 24px;">{{ order?.client_details.full_name }}</p>
        <p>{{ order?.machine_details.model.model }}</p>
        <BaseButton @click="$emit('close')" texto="Cerrar"/>
    </div>
</template>

<style scoped>
.modal-ot {
    position: fixed; 
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 9999;    
    width: 40rem;
    height: 50rem;
    padding: 1rem;
    border-radius: .5rem;
    border: 1px solid black;
    background-color: yellow;
    overflow-y: auto; 
}
</style>