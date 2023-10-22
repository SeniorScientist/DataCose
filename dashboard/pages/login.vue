<template>
  <section class="section">
    <h2 class="title has-text-centered">Welcome back!</h2>

    <Notification 
      v-if="error"
      :message="error" />

    <b-form @submit="login">
      
      <b-form-group 
        id="input-group-email" 
        label="Email address:" 
        label-for="input-email"
        description="We'll never share your email with anyone else.">
      
        <b-form-input 
          id="input-email" 
          v-model="credentials.email" 
          type="email" 
          placeholder="Enter email" 
          required />
      </b-form-group>

      <b-form-group 
        id="input-group-pwd" 
        label="Your Password:" 
        label-for="input-pwd">
      
        <b-form-input 
          id="input-pwd" 
          v-model="credentials.password"
          type="password" 
          placeholder="Enter your password"
          required />
      </b-form-group>

      <b-form-group id="input-group-confirm">
        <b-button variant="primary" type="submit">Primary</b-button>
      </b-form-group>
    
    </b-form>
  </section>
</template>
  
<script lang="ts">
import Notification from "~/components/Notification.vue"
import { Credentials } from "~/types/auth"


export default {
  components: {
    Notification,
  },

  data() {
    const credentials: Credentials = {
      email: '',
      password: '',
    }

    const error = ''

    return {
      credentials,
      error
    }
  },

  methods: {
    async login() {
      try {
        const response = await this.$auth.loginWith('local', {
          data: {
            email: this.credentials.email,
            password: this.credentials.password
          }
        })
        await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)
        this.$toast.success('Logged In!')
        this.$router.push({ path: "/author" })
      } catch (e) {
        console.log('error type', JSON.stringify(e))
        this.error = JSON.stringify(e)
      }
    }
  }
}
</script>