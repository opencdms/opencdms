<template>
  <v-card style="height: 600px;">
    <v-card-title>View feature</v-card-title>
    <base-map @mapLoaded="onMapLoaded" style="height: 100%;" zoom="4"/>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import BaseMap from "./../web-components/maps/base-map.vue"
import L from 'leaflet';
import {useRepo} from 'pinia-orm';
import Feature from '@/models/Feature';
import Wkt from 'wicket';


export default defineComponent({
  name: 'feature',
  props: {
    geom: {
      type: Object,
      required: false
    }
  },
  data() {
    return {
      map:null
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    BaseMap
  },
  methods: {},
  setup(props, context) {

    // lifecycle hooks
    onBeforeMount( () => {
      // This hook is called before the component is mounted to the DOM.
      // This is a good place to do any necessary setup before the component is visible.
    });
    onMounted( () => {
      // This hook is called after the component is mounted to the DOM.
      // This is a good place to perform any necessary DOM manipulations, initialize
      // third-party libraries, or set up event listeners.
    });
    onBeforeUpdate( () => {
      // This hook is called when a component's data changes, but before the DOM is re-rendered.
      // This is a good place to make any necessary calculations or changes before the component
      // is updated.
    });
    onUpdated( () => {
      // This hook is called after the component is updated and the DOM is re-rendered.
      // This is a good place to perform any necessary DOM manipulations or update third-party
      // libraries.
    });
    onBeforeUnmount( () => {
      // This hook is called before the component is unmounted from the DOM.
      // This is a good place to clean up any resources or event listeners that were set up in
      // onMounted.
    });
    onUnmounted( () => {
      // This hook is called after the component is unmounted from the DOM.
      // This is a good place to perform any final cleanup or tear down of resources.
    });
    const onMapLoaded = async (map) => {
      const feature = await useRepo(Feature).where("id",1).first();
      feature.properties = JSON.parse(feature.properties);
      console.log(feature.properties);
      // convert to geojson ust wkt
      var wkt = new Wkt.Wkt();
      wkt.read(feature.geometry);
      var geometry = wkt.toJson();
      var geojson = {
        "type": "Feature",
        "geometry": geometry,
        "properties": {
          "name": feature.name,
          "feature_type": "watershed",
          ...feature.properties
        }
      };
      console.log(geojson.properties)
      L.geoJSON(geojson, {
        onEachFeature: function (feature, layer ){
          layer.bindPopup("<h3>"+feature.properties.name+"</h3>" +
          "<p>Feature type: "+feature.properties.feature_type+"</p>" +
          "<p>Watershed level: "+feature.properties.watershed_level+"</p>" +
          "<p>Area: "+feature.properties.area*0.01+" km2</p>" +
          '<p>Attribution: <a href = "https://geohub.lio.gov.on.ca/maps/53a1c537b320404087c54ef09700a7db/explore?location=46.707978%2C-82.815433%2C2.80">Ontario Watershed Boundaries (OWB) collection, Ontario Ministry of Natural Resources and Forestry</a></p>'
            );
        }
      }).addTo(map);
    };
    onErrorCaptured( () => {});
    return {onMapLoaded};
  }

});
</script>
