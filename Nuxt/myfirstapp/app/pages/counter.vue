<template>
    <div>
        <h1>Into the counter app basics</h1>
        <button @click="add">+</button>
        <p>{{ counter.count}}</p>
           <p>{{ counter.double}}</p>
        <button @click="sub">-</button>
    </div>
</template>

<script setup>
import { useCouterStores } from '#imports';
const counter  = useCouterStores()
function add(){
    counter.increment()
}
function sub(){
    counter.decrement()
}
</script>