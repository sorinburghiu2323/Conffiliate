<template>
  <div v-if="!business">
    <h2>
      Your Fanbase...
    </h2>
    <input type="number" :step=20 :min=0 v-model="audNumber" placeholder="Audience Number"/>
    <input type="number" :step=10 :min=0 v-model="avgPosts" placeholder="Average views/posts"/>
    <div>
      <select v-model="selected">
        <option disabled value="">Platform</option>
        <option>A</option>
        <option>B</option>
        <option>C</option>
      </select>
      <span>{{ selected }}</span><br>
      <input type="url" v-model="platLink" placeholder="Link"/>
    </div>
  </div>
  <div v-else-if="business">
    <h2>
       Your Business...
    </h2>
    <input type="text" v-model="businessName" placeholder="Business name"/><br>
    <input type="url" v-model="businessLink" placeholder="Website link"/><br>
    <input type="number" v-model="avgPay" placeholder="Avg. Pay offered"/>
  </div>
</template>

<script>
export default {
  name: "Step4",
  data() {
    return {
      selected: '',
      audNumber: null,
      avgPosts: null,
      platLink: null,
      businessName: null,
      businessLink: null,
      avgPay: null,
    };
  },
  props: {
    business: Boolean,
  },
};
</script>

<style scoped>

</style>