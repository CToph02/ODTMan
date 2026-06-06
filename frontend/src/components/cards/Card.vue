<script setup>
</script>

<template>
    <div class="card">
        <div class="col">
            <p>Nombre cliente: </p>
            <p>Tipo de máquina:</p>
            <p>Marca:</p>
            <p>Modelo:</p>
        </div>
        
        <div class="col-2">
            <p>N° orden:</p>
            <p>Estado:</p>
        </div>
    </div>
</template>

<style scoped>
.card{
    width: 24rem;
    border: 1px solid gray;
    border-radius: 8px;
    padding: 8px;
    box-shadow: black;
    display: flex;
    flex-direction: row;
    gap: 8rem;
    box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.2);
}
.col{
    display: flex;
    flex-direction: column;
}
.col-2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
</style>