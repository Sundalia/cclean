<template>
  <div class="header_text">
    <div class="main_h2__header_box">
      <h2 class="main_h2">{{ header }}</h2>
    </div>
    <div class="main_h2__text_box">
      <p class="main_h2__text">
        {{ text }}
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HeaderText',
    props: {
      header: {
        type: String,
        required: true
      },
      text: {
        type: String,
        required: true
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>