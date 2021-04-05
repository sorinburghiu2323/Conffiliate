<template>

  <h2>
    About yourself...
  </h2>
  <div v-if="!is_business">
      Currently selected Influencer
  </div>
  <div v-else-if="is_business">
      Currently selected Business
  </div>
  <input type="text" v-model="name" placeholder="Name"/>
  <input type="text" v-model="email" placeholder="Email"/>
  <div v-if="!is_business">
      <input type="text" v-model="aka" placeholder="Known as"/>
  </div>
  <input type="text" v-model="phone" placeholder="Phone number"/>
</template>

<script>
export default {
  name: "Step2",
  data() {
    return {
      name: '',
      email: '',
      aka: '',
      phone: '',
    }
  },
  props: {
    is_business: Boolean,
  }
}
</script>

<style scoped>
</style>
