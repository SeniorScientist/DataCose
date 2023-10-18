<template>
    <div class="notification is-danger">
        {{ message }}
    </div>
</template>
  
<script lang="ts">

export default {
    name: 'Notification',
    props: ['message']
}
</script>