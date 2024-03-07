 <template>
    <q-layout>
        <q-page class="springpage">
            <CleanTypeBanner :header="header"/>
            <BreadCrumbs :breadcrumb="breadcrumb"/>
            <MainForm/>
            <HeaderText :header="headertext_header" :text="headertext_text"/>
            <WhatIncludeSpring/>
            <ConnectLinks/>
            <AppBanner/>
            <FeedBack/>
        </q-page>
    </q-layout>
</template>

<script>
import CleanTypeBanner from 'components/CleanTypeBanner.vue'
import BreadCrumbs from 'components/BreadCrumbs.vue'
import MainForm from 'components/MainForm.vue'
import HeaderText from 'components/HeaderText.vue'
import WhatIncludeSpring from 'src/components/spring_page/WhatIncludeSpring.vue'
import ConnectLinks from 'src/components/ConnectLinks.vue'
import AppBanner from 'src/components/AppBanner.vue'
import FeedBack from 'src/components/FeedBack.vue'

export default({
    name: 'SpringPage',
    components: {
        CleanTypeBanner,
        BreadCrumbs,
        MainForm,
        HeaderText,
        WhatIncludeSpring,
        ConnectLinks,
        AppBanner,
        FeedBack
    },
    data() {
        return {
            header: 'генеральная уборка в санкт-петербурге от 5000 рублей',
            breadcrumb: 'Генеральная',
            headertext_header: 'что входит в генеральную уборку',
            headertext_text: 'Генеральная уборка - важная часть поддержания чистоты. В отличие от повседневной уборки, в том, что мы акцентируем свое внимание на труднодоступных местах. Это очень важно, так как это продлит срок службы вашей мебели, предметов интерьера и общую чистоту. Генеральная уборка – это полное очищение всех видов поверхностей помещения, включая потолки, стены и труднодоступные места. Главное отличие генеральной уборки от привычной поддерживающей – удаление застарелых загрязнений и локальных пятен.'
        }
    },
    mounted() {
        
    }
})
</script>

<style lang="scss" scope>
</style>