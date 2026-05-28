<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import BaseButton from '@/components/buttons/BaseButton.vue';
import { authService } from '@/services/auth.js';

const username = ref('');
const password = ref('');
const router = useRouter();

const handleSubmit = async () => {
    if (!username.value || !password.value) return;

    try {
        await authService.login({
            username: username.value,
            password: password.value
        });
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
    <h1>HOLA</h1>
    <div class="login-form">
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="user">Username</label>
                <input id="user" v-model="username" type="text" required>
            </div>
            <div class="form-group">
                <label for="pass">Password</label>
                <input id="pass" v-model="password" type="password" placeholder="·········" required>
            </div>
            <div class="btn-auth">
                <BaseButton
                    texto="Iniciar sesión"
                    color="blue"
                    type="submit"
                />
            </div>
        </form>
    </div>
</template>

<style scoped>
.form-group{
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.btn-auth{
    display: flex;
    gap: 8px;
}
</style>