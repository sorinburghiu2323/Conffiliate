<template>
  <h1>Register</h1>
  <h2>Let's get you connected at no cost.</h2>
  <div class="form-container">
    <div class="progress-bar"></div>
    <div v-if="step === 1">
      <Step1
        @is_business="setBusiness"
        @influencer="setInfluencer"
        @nextStep="goNext"
      ></Step1>
    </div>
    <div v-else-if="step === 2">
      <Step2 :is_business="is_business"></Step2>
    </div>
    <div v-else-if="step === 3">
      <Step3></Step3>
    </div>
    <div v-else-if="step === 4">
      <Step4 :is_business="is_business"></Step4>
    </div>
    <div class="bottom-nav">
      <button name="back" @click.prevent="goBack">Back</button>
      <button name="next" @click.prevent="goNext">Next</button>
    </div>
  </div>
</template>

<script>
import Step1 from "../components/RegisterSteps/Step1.vue";
import Step2 from "../components/RegisterSteps/Step2.vue";
import Step3 from "../components/RegisterSteps/Step3.vue";
import Step4 from "../components/RegisterSteps/Step4.vue";
export default {
  name: "Register",
  data() {
    return {
      step: 1,
      is_business: false,
    };
  },
  components: {
    Step1,
    Step2,
    Step3,
    Step4,
  },
  methods: {
    goNext() {
      if (this.step < 5) {
        this.step++;
      }
    },
    goBack() {
      if (this.step > 1) {
        this.step--;
      }
    },
    setBusiness() {
      this.is_business = true;
    },
    setInfluencer() {
      this.is_business = false;
    },
  },
};
</script>

<style scoped>
@import "../assets/css/progress-bar.css";
.form-container {
  padding-top: 4px;
  width: max(500px, 40%);
  padding-bottom: 10px;
  border-radius: 20px;
  border: 1px solid black;
  margin: auto;
}

.bottom-nav {
  padding: 4px;
}
</style>
