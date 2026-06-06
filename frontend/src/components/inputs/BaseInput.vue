<script setup>
const model = defineModel(
    {
        type: String, 
        default: ""
})

defineProps({
    placeholder:{
        type: String,
        default: ""
    },
    label:{
        type: String,
        default: ""
    },
    type:{
        type: String,
        default: 'text'
    },
    name:{
        type: String,
        required: true
    }
})
</script>

<template>
    <div class="input-group">
        <label v-if="label" :for="name">
            {{ label }}
        </label>
        <input v-model="model" :id="name" :type="type" :placeholder="placeholder">
    </div>    
</template>

<style scoped>
.input-group{
    gap: .5rem;
    margin: 1rem;
    display: flex;
    flex-direction: column;
}
input{
    padding: 4px;
    border: 1px solid black;
    border-radius: 4px;
}
</style>