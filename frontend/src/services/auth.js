import api from "@/api/axios";

export const authService = {
    register(data) {
        return api.post('auth/register/', data)
    },

    login(data){
        return api.post('auth/login/', data)
    },

    logout(data){
        return api.post('auth/logout/', data)
    },
    getUser(){
        return api.get('auth/user/')
    }
}