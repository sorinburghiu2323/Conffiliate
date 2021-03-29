<template>
  I am a...
  <div class="select">
    <button name="Business" type="submit" @click.prevent="route('business')">Business</button>
    <button name="Influencer" type="submit" @click.prevent="">Influencer</button>
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

</style>