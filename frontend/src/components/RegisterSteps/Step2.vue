<template>
  <input type="text" v-model="name"/>
  <input type="text" v-model="email"/>
  <div v-if="!business">
      <input type="text" v-model="aka"/>
  </div>
  <input type="text" v-model="phone"/>
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