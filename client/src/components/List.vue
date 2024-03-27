<script setup>
import { add_item, get_list } from '../api.js'

const model = defineModel()
const name = ""

async function create() {
    await add_item(model.value.list.id, name)
    model.value.list = await get_list(model.value.list.id)
}
</script>

<template v-if="model.value.list">
    <h1>{{ model.value.list.name }}</h1>
    <ul>
        <li v-for="item in model.value.list.items">
            {{ item.name }}
        </li>
    </ul>
    <input type="string" v-model="name" placeholder="Name of new item"><br>
    <button >Create</button>
</template>