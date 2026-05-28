import api from "@/api/axios";

export const machineService= {
    getAll() {
        return api.get('machines/')
    }
}