<template>
  <v-card style="height: 100%; width: 100%;">
  <station-map style="height: 100%;"/>
  </v-card>
</template>

<script>
import StationMap from './../web-components/station-map.vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/lib/components';
import BaseMap from './../web-components/maps/base-map.vue'

export default {
  components: {
    StationMap,
    BaseMap,
    VCard,
    VCardTitle
  },
};
</script>

<style>
  #map{
    width: 100%;
    height: 100%;
  }
</style>

