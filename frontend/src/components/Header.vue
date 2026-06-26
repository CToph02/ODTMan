<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router';
import { authService } from '@/services/auth.js';
import BaseButton from '@/components/buttons/BaseButton.vue'

const nombre = ref('')
const router = useRouter();

const handleLogout = async () => {
    try{
        const refreshToken = localStorage.getItem('refresh');
        await authService.logout({'refresh': refreshToken});
    }catch (error){
        console.log('El token ya expiró', error);
    }finally{
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        router.push('/');
    }
}

onMounted(async () => {
    try{
        const response = await authService.getUser()
        nombre.value = response.data.username
    }catch{
        console.log('Error al obtener los datos del usuario.')
    }
})
</script>

<template>
    <header>
        <span>Hola, {{nombre}}</span>
        <h1>ODTMan</h1>
        <div>
            <BaseButton
                texto="Cerrar sesión"
                color="green"
                @click="handleLogout"
            />
        </div>
    </header>
    
</template>

<style scoped>
header{
    padding: 1rem;
    height: 3rem;
    background-color: gray;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}
header span{
    font-size: 24px;
    font-weight: bold;
}
</style>