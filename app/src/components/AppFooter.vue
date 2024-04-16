<template>
  <v-footer>
    <div >
      <a href="#" target="_blank">OpenCDMS</a>
      <span class="ms-1">&copy; {{ new Date().getFullYear() }} OpenCDMS.</span>
    </div>
    <div class="ms-auto">
      <span class="me-1" target="_blank">Powered by</span>
      <a href="#">OpenCDMS</a>
    </div>
  </v-footer>
</template>

<script>
  import { VFooter } from 'vuetify/lib/components'
  export default {
    name: 'AppFooter',
    components: {
      VFooter
    },
  };
</script>
