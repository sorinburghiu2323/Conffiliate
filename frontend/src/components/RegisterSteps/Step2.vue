<template>
  <h2>
    About you...
  </h2>
  <input type="text" v-model="name" placeholder="Name"/>
  <input type="text" v-model="email" placeholder="Email"/>
  <div v-if="!business">
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
    business: Boolean,
  }
}
</script>

<style scoped>

</style>