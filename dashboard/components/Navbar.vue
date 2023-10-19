<template>
  <div>
    <b-navbar type="dark" variant="success" toggleable="lg">
      <b-navbar-brand href="/">Nuxt Auth</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">
            <nuxt-link class="navbar-item" to="/author">Authors</nuxt-link>
          </b-nav-item>
          <b-nav-item href="#" disabled>
            <nuxt-link class="navbar-item" to="/book">Books</nuxt-link>
          </b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav right v-if="loggedIn">
          <nuxt-link class="navbar-item" to="/register">Log out</nuxt-link>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script lang="ts">

export default {
  data() {
    const loggedIn: Boolean = this.$auth.loggedIn || false
    return {
      loggedIn
    }
  },

  watch: {
    loggedIn(newQuestion, oldQuestion) {
      if (newQuestion) {
        this.loggedIn = this.$auth.loggedIn
      }
    }
  }
}
</script>
