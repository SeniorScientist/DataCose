<template>
  <div>
    <b-navbar type="dark" variant="light">
      <b-navbar-brand href="/">Nuxt Auth</b-navbar-brand>

      <b-nav-item-dropdown class="ml-auto" text="User" right>
        <b-dropdown-item href="#">
          <nuxt-link class="navbar-item" to="/register">Register</nuxt-link>
        </b-dropdown-item>
        <b-dropdown-item href="#">
          <nuxt-link class="navbar-item" to="/login">Log In</nuxt-link>
        </b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar>
  </div>
</template>
