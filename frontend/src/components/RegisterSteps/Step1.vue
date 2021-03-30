<template>
  <h2>I am a...</h2>
  <div class="select">
    <div class="business" @click.prevent="route('business')"><h2>Business</h2></div>
    <div class="influencer" @click.prevent="route('influencer')"><h2>Influencer</h2></div>
  </div>
</template>

<script>
export default {
  name: "Step1",
  emits: {
    business: null,
    nextStep: null,
  },
  methods: {
    route(type){
      console.log(type)
      this.$emit(type);
      this.$emit("nextStep");
    }
  }
}
</script>

<style scoped>
.select {
  margin: auto;
  position: relative;
  display: flex;
}
.business {
  margin-left:auto;
  border-radius: 10px 0 0 10px;
  cursor: pointer;
  padding-left: 4px;
  padding-right: 4px;
  border: 1px solid black;
}
.influencer {
  margin-right: auto;
  border-radius: 0 10px 10px 0;
  cursor: pointer;
  padding-left: 4px;
  padding-right: 4px;
  border: 1px solid black;
}
</style>