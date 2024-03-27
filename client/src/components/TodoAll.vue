<script setup>
import { all_lists } from '../api.js'
const lists = await all_lists()
</script>

<template>
    <ul>
        <li v-for="l in lists">
            <button>{{ l.name }}</button>
        </li>
    </ul>
    <button>
        New Todo List
    </button>
</template>