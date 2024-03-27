<script setup>
import { get_list, modify_item } from '../api.js'

const model = defineModel()

async function save() {
    await modify_item(model.value.item.id, model.value.item)
}

async function back() {
    model.value.list = await get_list(model.value.item.list_id)
    model.value.which = "list"
}
</script>

<template>
    <input type="string" v-model="model.value.item.name"><br>
    <button @click="async () => save()">Save</button><br>
    <button @click="async () => back()">Back to todo list</button>
</template>