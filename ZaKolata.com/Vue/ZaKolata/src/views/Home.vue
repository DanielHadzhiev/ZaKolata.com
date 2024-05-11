<template>
  <LoginForm v-if="showLogin"></LoginForm>
  <section class="welcome-screen">
    
  </section>
  <section class="top-products">

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

<style></style>

<script setup>
import LoginForm from '@/components/LoginForm.vue'
</script>
