<template>
      <base-map @mapLoaded="onMapLoaded" style="height: 100%;" zoom="4" :id="id"/>
</template>


<script>
// geojson validator
import * as gjv from 'geojson-validation';

// Leaflet
import L from 'leaflet';

// vue imports
import { defineComponent, ref, computed, watch } from 'vue';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';

// vuetify imports
import { VCard, VCardTitle, VCardText, VCardItem } from 'vuetify/lib/components';

// OpenCDMS imports
import BaseMap from "@/web-components/maps/base-map.vue"

export default defineComponent({
  name: "FeatureMap",
  props: {
    geom: {
      type: Object,
      required: false
    },
    id: {
      type: String,
      default: "map"
    }
  },
  components: {
    VCard, VCardTitle, VCardItem, VCardText,
    BaseMap
  },
  setup( props, context ){
    const map = ref(null);
    const markerLayer = ref(null);
    const onMapLoaded = async (mapInstance) => {
      console.log( props.id )
      map.value = mapInstance;
      if ( props.geom ){
        // make sure the geometry is valid
        if( gjv.isFeature(props.geom) ){
          // now add to map
          markerLayer.value = L.geoJSON(props.geom).addTo(map.value);
          map.value.fitBounds(markerLayer.value.getBounds());
          map.value.setZoom(6);
        }else{
          console.log("invalid geom"); // data race ToDo fix
          markerLayer.value = L.geoJSON(props.geom).addTo(map.value);
          map.value.fitBounds(markerLayer.value.getBounds());
          map.value.setZoom(6);
        }
      }else{
        console.log("No geometry");
      }
    };
    watch( () => props.geom, (newValue) => {
      if( markerLayer.value ){
        markerLayer.value.remove();
      }
      markerLayer.value = L.geoJSON(newValue).addTo(map.value);
      map.value.fitBounds(markerLayer.value.getBounds());
      map.value.setZoom(6);
    })
    return {map, onMapLoaded};
  }
});

</script>
