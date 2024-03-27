<script setup>
import { reactive, onMounted } from 'vue'
import { all_lists } from './api.js'
import Lists from './components/Lists.vue'
import List from './components/List.vue'
import Item from './components/Item.vue'

const state = reactive(
    {
        which: "all",
        lists: [],
        list: null,
        item: null
    }
)

onMounted(async () => { state.lists = await all_lists() })
</script>

<template>
    <Lists v-show="state.which == 'all'" v-model="state"></Lists>
    <List v-show="state.which == 'list'" v-model="state"></List>
    <Item v-show="state.which == 'item'" v-model="state"></Item>
</template>