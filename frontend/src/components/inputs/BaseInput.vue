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
    padding: 1rem;
    border: 1px solid gray;
    border-radius: .5rem;
    width: 10rem;
    transition: .25s ease-in-out;
}

input:hover{
    border: 1px solid black;
}

/* input:focus{
    width: 25rem;
} */

</style>