<template>
  <div>
    <swiper
      :slidesPerView="6"
      :spaceBetween="30"
      :freeMode="true"
      :pagination="{
        clickable: true,
      }"
      :modules="modules"
      class="feedback__swiper"
    >
      <swiper-slide v-for="i in 10" :key="i">
        <FeedBackCell/>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import FeedBackCell from './subcomponents/FeedBackCell.vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { FreeMode, Pagination } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/free-mode'
import 'swiper/css/pagination'


  export default {
    name: 'FeedBack',
    components: {
      FeedBackCell,
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        
      }
    },
    setup() {
      return {
        modules: [FreeMode, Pagination],
      }
    }
  }
</script>

<style lang="scss" scoped>

.feedback__swiper{
  padding: 2%;
}

</style>