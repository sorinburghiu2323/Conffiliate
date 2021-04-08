<template>
  <h2>Description...</h2>
  <input
    class="textarea"
    type="text"
    v-model="bio"
    placeholder="About yourself or your business..."
  />
  <input
    class="textarea"
    type="text"
    v-model="keywords"
    placeholder="Keywords..."
  />
</template>

<script>
export default {
  name: "Step3",
  data() {
    return {
      bio: "",
      keywords: "",
    };
  },
  props: {
    is_business: Boolean,
  },
};
</script>

<style scoped>
.textarea {
}
</style>
