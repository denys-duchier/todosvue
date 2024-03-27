<script setup>
import { reactive } from 'vue'
import { all_lists } from '../api.js'
const state = reactive(
    {
        which: "all",
        lists: [],
        list: null,
        item: null
    }
)
state.lists = await all_lists()
</script>

<template>
    <Lists v-show="state.which.value == 'all'" v-model="state"></Lists>
    <List v-show="state.which.value == 'list'" v-model="state"></List>
    <Item v-show="state.which.value == 'item'" v-model="state"></Item>
</template>