<template>
  <v-container style="width: 100%;">
    <v-row>
      <v-col :cols=12>
        <v-row>
          <v-col :cols=12><geometry-picker v-model="geom" style="height: 100%" @geometry-selected="updateGeom"/></v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import GeometryPicker from './../web-components/pickers/geometry.vue';
import { VCard, VCardTitle, VCardText, VForm, VTextField } from 'vuetify/lib/components';
import { VContainer, VRow, VCol } from 'vuetify/lib/components';
import BaseMap from './../web-components/maps/base-map.vue'

export default {
  components: {
    GeometryPicker,
    BaseMap,
    VCard,
    VCardTitle,
    VContainer,
    VRow,
    VCol, VForm, VTextField
  },
  data() {
    return {
      geom: null
    }
  },
  methods: {
    updateGeom(geometry) {
      console.log(geometry)
      this.geom = geometry;
    }
  }
};
</script>

<style>
  #map{
    width: 100%;
    height: 100%;
  }
</style>

