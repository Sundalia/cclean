<template>
    <q-layout>
        <q-page-container>
            <header-item/>
            <router-view/>
        </q-page-container>
    </q-layout>
</template>

<script>
import HeaderItem from 'src/components/HeaderItem.vue';


export default({
    name: 'AccountLayout',
    components: [
        HeaderItem
    ]
})
</script>
