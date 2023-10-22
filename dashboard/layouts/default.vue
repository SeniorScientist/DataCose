<template>
  <b-container>
    <NavBar />
    <div class="flex p-4 items-center justify-center">
      <nuxt />
    </div>
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
