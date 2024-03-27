<script setup>
import { add_list } from '../api.js'

const model = defineModel()
const name = ""

async function new_list() {
    const json = await add_list({ "name": name })
    model.value.list = json
    model.value.which = "list"
}
</script>

<template>
    <ul v-if="model.value">
        <li v-for="list in model.value.lists">
            {{ list.name }}
        </li>
    </ul>
    <input v-model="name" type="string" placeholder="Name of todo list"><br>
    <button @click="async () => new_list()">Create</button>
</template>