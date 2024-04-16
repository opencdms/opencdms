<template>
  <v-app>
    <AppSidebar app/>
    <AppHeader app/>
    <v-main app>
      <v-container fluid class="justify-center align-center text-h5" style="height: calc(100vh - 110px); overflow:auto; padding: 10px;">
         <router-view/>
      </v-container>
    </v-main>
    <AppFooter app/>
  </v-app>
</template>

<script>
  import { VApp } from 'vuetify/lib/components';
  import { VMain, VContainer, VNavigationDrawer } from 'vuetify/lib/components';
  import AppSidebar from '@/components/AppSidebar';
  import AppHeader from '@/components/AppHeader';
  import AppFooter from '@/components/AppFooter';
  export default {
    components: {
      VApp,
      VMain,
      VContainer,
      AppHeader,
      AppSidebar,
      AppFooter
    },
  };
</script>

