import api from "@/api/axios";

export const machineService = {
    getAll() {
        return api.get('machines/units/')
    },
    getMachine(id){
        return api.get(`machines/units/${id}`)
    }
}