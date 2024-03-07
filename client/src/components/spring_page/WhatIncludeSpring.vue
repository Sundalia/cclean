<template>
  <div class="what_include_container">
    <div class="row what_include_grid">
    <WhatIncludeCol
      img_src="kitchen.svg" 
      img_header="на кухне:"
      :what_include="what_include_spring_kitchen" 
      :can_add = "can_add_spring_kitchen"
    />
    <WhatIncludeCol 
      img_src="room.svg" 
      img_header="в комнатах:"
      :what_include="what_include_spring_room"
    />
    <WhatIncludeCol 
      img_src="bathroom.svg" 
      img_header="в санузлах:"
      :what_include="what_include_spring_bathroom"
    />
  </div>
  </div>
</template>

<script>
import WhatIncludeCol from 'components/subcomponents/WhatIncludeCol.vue'

  export default {
    name: 'WhatIncludeSpring',
    components: {
      WhatIncludeCol
    },
    data() {
      return {
        what_include_spring_kitchen: [],
        what_include_spring_room: [],
        what_include_spring_bathroom: [],
        can_add_spring_kitchen: []
      }
    },
    methods: {
    },
    mounted() {
      this.$api.get("/cleaning_type/1.json")
        .then(res => {
          console.log(res.data)
          this.what_include_spring_kitchen = res.data.location[0].include.map((i) => i)
          this.what_include_spring_room = res.data.location[1].include.map((i) => i)
          this.what_include_spring_bathroom = res.data.location[2].include.map((i) => i)

          this.can_add_spring_kitchen = res.data.location[0].can_add.map((i) => i)
          console.log(this.can_add_spring_kitchen)
        })
        .catch(err => console.log(err))
    }
  }
</script>

<style lang="scss" scoped>

.what_include_container{
  display: flex;
  justify-content: center;
  margin: 2%;
}

.what_include_grid{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  width: 100%;
}

@media screen and (max-width: 820px){
  .what_include_grid{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 520px){
  .what_include_grid{
    display: grid;
    grid-template-columns: repeat(1, 1fr);
  }
}

</style>