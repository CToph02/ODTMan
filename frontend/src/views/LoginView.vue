<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import BaseButton from '@/components/buttons/BaseButton.vue';
import { authService } from '@/services/auth.js';
import BaseInput from '@/components/inputs/BaseInput.vue';

const username = ref('');
const password = ref('');
const router = useRouter();

const handleSubmit = async () => {
    if (!username.value || !password.value) return;

    try {
        const response = await authService.login({
            username: username.value,
            password: password.value
        });
        localStorage.setItem('access', response.data.access)
        localStorage.setItem('refresh', response.data.refresh)
        router.push('/home');
    }
    catch (error) {
        if (error.response) {
            console.log('Django dice que el error es:', error.response.data);
        } else {
            console.log('Error general:', error.message);
        }
    }
}
</script>

<template>
    <div class="login-container">
        <div class="login-form">
            <h1>Bienvenido</h1>
            <form @submit.prevent="handleSubmit">
                <BaseInput v-model="username" name="user" label="Username" type="text" />
                <BaseInput v-model="password" name="password" label="Password" type="password" placeholder="·························"/>
                <div class="btn-auth">
                    <BaseButton
                        texto="Iniciar sesión"
                        color="blue"
                        type="submit"
                    />
                </div>
            </form>
        </div>
    </div>
    
</template>

<style scoped>
.login-container{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100vw;
}
.login-form{
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid black;
    border: 1px solid black;
    border-radius: 4px;
    padding: 1rem;
}
form{
    width: 100%;
}
.btn-auth{
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 1rem;
}
</style>