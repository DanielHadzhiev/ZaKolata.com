<template>
  <section class="welcome-screen">
    
  </section>
  <section class="top-products">
    <h1>ТОП 10 ПРОДУКТА</h1>
  </section>
  <section class="about-us">

  </section>
</template> 

<script>
export default {
  data() {
    return {
      showLogin: true,
    };
  },
  components: {
    LoginForm
  },
  methods: {
    toggleLoginForm() {
      this.showLogin = !this.showLogin
    },
    handleEscapeKey(event) {
      if (event.key === 'Escape') {
        this.showComponent = false;
      }
    }
  }, 
  mounted() {
    window.addEventListener('keydown', this.handleEscapeKey);
  },
  beforeDestroy() {
    window.removeEventListener('keydown', this.handleEscapeKey);
  }
};
</script>

<style scoped>
  .welcome-screen {
    height: 700px;
    background: url('../assets/imgs/welcome-bg.jpg') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }

  .top-products {
    height: 400px;
    color: white;
    background-color: rgb(43, 43, 43);
  }

  .top-products h1 {
    text-align: center;
    margin: 0;
    padding-top: 30px;
  }

</style>

<script setup>
import LoginForm from '@/components/LoginForm.vue'
</script>
