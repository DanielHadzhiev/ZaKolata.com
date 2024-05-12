<template>
    <main>
      <Nav :isLogin="isLogin"></Nav>
      <router-view></router-view> <!-- Where routed views are rendered -->
    </main>
    <Footer></Footer>

</template> 

<script>
  import Nav from './components/Nav.vue'
  import Footer from './components/Footer.vue'

  export default {
   components: {
    Nav
   },
   data() {
      return {
        isLogin: false,
      }
   }
  };
</script>
  
<style></style>
  
<script setup>
  import Nav from './components/Nav.vue'
</script>
  
<style>
  html, body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
</style>