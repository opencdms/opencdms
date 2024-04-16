<template>
  <v-app-bar>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-app-bar-title>OpenCDMS Demo</v-app-bar-title>
  </v-app-bar>
</template>
<script>
  import { VAppBar, VAppBarNavIcon, VAppBarTitle } from 'vuetify/lib/components'
  export default {
    name: 'AppHeader',
    components: {
      VAppBar,
      VAppBarNavIcon,
      VAppBarTitle
    },
  };
</script>
