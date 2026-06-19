import api from "@/api/axios";

export const orderService = {
    getAll() {
        return api.get('orders/odt/')
    },
    getOrderById(id){
        return api.get(`orders/odt/${id}`)
    }
}