<template>
    <q-layout>
        <q-page-container class="indexpage">
            <MaiBanner/>
            <MainForm/>
            <WhyWe/>
            <OurServices/>
            <WeDid/>
            <OurPartners/>
            <MainFeedback/>
            <ConnectLinks/>
            <MainAppBanner/>
        </q-page-container>
    </q-layout>
</template>

<script>
import MaiBanner from 'components/index_page/MainBanner.vue'
import MainForm from 'components/MainForm.vue'
import WhyWe from 'src/components/index_page/WhyWe.vue';
import OurServices from 'src/components/index_page/OurServices.vue';
import WeDid from 'src/components/index_page/WeDid.vue';
import OurPartners from 'src/components/index_page/OurPartners.vue';
import MainFeedback from 'src/components/index_page/MainFeedback.vue';
import ConnectLinks from 'src/components/ConnectLinks.vue';
import MainAppBanner from 'src/components/index_page/MainAppBanner.vue';


export default({
    name: 'IndexPage',
    components: {
        MaiBanner,
        MainForm,
        WhyWe,
        OurServices,
        WeDid,
        OurPartners,
        MainFeedback,
        ConnectLinks,
        MainAppBanner

    }
})
</script>

<style lang="scss" scoped>
</style>