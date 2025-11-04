import { defineStore } from "pinia";

export const useCouterStores = defineStore('counter',{
    state:()=>({
       count:0
    }),

    getters:{
        double:(state)=>state.count-2
    },
    actions:{
        increment(){
            this.count++
        },
        decrement(){
            if(this.count<=0)
                return
           this.count--
        }
    }
})
