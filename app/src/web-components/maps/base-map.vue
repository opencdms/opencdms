<template>
  <v-card style="width: 100%; height: 100%;" id="map" :selectEnables="selectEnabled"></v-card>
</template>

<script>
import { defineComponent, ref, computed, onMounted } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/lib/components';
import "leaflet/dist/leaflet.css";
import L from 'leaflet'
import "leaflet-lasso";

export default defineComponent({
  name: "base-map",
  props: {
    center: {
      type: Object,
      default: () => ({ lat: 46.223240947638416, lng: 6.146185398101807 })
    },
    zoom: {
      type: Number,
      default: 16
    },
    selectEnabled: {
      type: Boolean,
      default: false
    }
  },
  data(){
    return {
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
  },
  setup( props, {emit} ) {
    const mapContainer = ref("map");
    const map = ref(null);
    onMounted( () =>{
      map.value = L.map(mapContainer.value, {zoomAnimation:false, fadeAnimation:true, markerZoomAnimation:true}).setView( props.center, props.zoom );
      map.value.attributionControl.setPrefix('<a href="https://leafletjs.com/">Leaflet</a>')
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; OpenStreetMap contributors'}).addTo(map.value);
      emit('mapLoaded', map.value);
      //if ( props.selectEnabled ){
      //  const lasso = new L.Control.Lasso();
      //  map.value.addControl(lasso)
      //}
    });

    return {mapContainer};
  }
})
</script>
