<script setup>
defineProps({
    order:{
        type: Object,
        default: null
    }
})
</script>

<template>
    <div class="card">
        <div class="col">
            <p>Nombre cliente: {{ order?.client_details.full_name }}</p>
            <p>Tipo de máquina: {{ order?.machine_details.model.category.category }}</p>
            <p>Marca: {{ order?.machine_details.model.brand.brand }}</p>
            <p>Modelo: {{ order?.machine_details.model.model }}</p>
        </div>
        
        <div class="col-2">
            <p>N° orden: {{ order?.machine_details.serial_number }}</p>
            <p>Estado: {{ order?.repair_status_details.status }}</p>
        </div>
    </div>
</template>

<style scoped>
.card{
    width: 25rem;
    height: 10rem;
    border: 1px solid gray;
    border-radius: .5rem;
    padding: 1rem;
    display: flex;
    flex-direction: row;
    gap: 8rem;
    transition: .1s ease-in;
    background-color: whitesmoke;
}

.card:hover{
    cursor: pointer;
    box-shadow: 6px 6px 15px rgba(0, 0, 0, 0.2);
    transform: scale(1.008);
}

.col{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.col-2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
</style>