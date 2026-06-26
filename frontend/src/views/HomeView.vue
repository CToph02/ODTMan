<script setup>
import Header from '@/components/Header.vue';
import Card from '@/components/cards/Card.vue';
import BaseInput from '@/components/inputs/BaseInput.vue';
import BaseButton from '@/components/buttons/BaseButton.vue';
import ModalOT from '@/components/Modal/ModalOT.vue';

import { onMounted, ref } from 'vue';

import { orderService } from '@/services/orders';

const data = ref([]);
const isModalOpen = ref(false);
const selectedOrder = ref(null);

onMounted(async () => {
    try{
        const response = await orderService.getAll();
        data.value = response.data;
    }catch (error){
        console.log(error);
    }
})

const openCreateModal = () => {
    selectedOrder.value = null;
    isModalOpen.value = true;
}

const openModal = () => {
    selectedOrder.value = data.value;
    isModalOpen.value = true;
}

const closeModal = () => {
    selectedOrder.value = null;
    isModalOpen.value = false;
}

</script>

<template>
    <Header/>
    <div class="a">
        <section class="cards-input">
            <div class="search-create">
                <BaseInput placeholder="Buscar OT" name="buscar"/>
                <BaseButton texto="Crear nueva OT" @click="openCreateModal"/>
            </div>
            <div class="cards">
                <Card v-for="order in data" :key="order.id" :order="order" @click="openModal"/>
            </div>
        </section>
    </div>
    
    <ModalOT v-if="isModalOpen" :order="selectedOrder" @close="closeModal"/>
    
</template>

<style scoped>
.search-create{
    width: 50%;
    display: flex;
    justify-content: space-evenly;
}
.cards{
    display: flex; 
    flex-wrap: wrap; 
    gap: .25rem; 
    justify-content: center; 
    width: 75%; 
    height: 100%;
}

.cards-input{
    display: flex;
    flex-direction: column;
    align-items: center;
}

@media (width: 728px) {
    .cards{
        width: 60%;
    }
}
</style>