<template>
  <b-container fluid>
    <NavBar />
    <nuxt />
  </b-container>
</template>

<script>
import NavBar from "~/components/Navbar.vue"

export default {
  components: {
    NavBar,
  },
};
</script>
