<template>
  <base-map @mapLoaded="onMapLoaded" :center="mapCenter" :zoom="zoom"/>
</template>

<script>
  // Leaflet imports
  import "leaflet/dist/leaflet.css";
  import "leaflet.markercluster/dist/MarkerCluster.css";
  import "leaflet.markercluster/dist/MarkerCluster.Default.css";
  import L from 'leaflet';
  import 'leaflet.markercluster';

  // vue / vuetify imports
  import { defineComponent, ref, watchEffect, watch } from 'vue';
  import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';

  import {useRepo} from 'pinia-orm';

  // opencdms imports
  import BaseMap from "./../web-components/maps/base-map.vue"
  import Host from '@/models/Host';
  import {loadData} from '@/utils/load-data.js';

  export default defineComponent({
    name: 'station-map',
    props: {
      connection: {
        type: String,
        default: "/data/hosts.psv"
      },
      mapCenter:{
        type: Object,
        default: () => ({ lat: 46.3097, lng: -79.4625 })
      },
      zoom: {
        type: Number,
        default: 8
      }
    },
    data() {
      return {
        map: null,
        //data: null,
        //geojson: null,
        //selected: new Set(),
      }
    },
    components: {
      BaseMap
    },
    methods: {},
    setup(props, context) {
      const features = ref([]);
      const hostRepo = useRepo(Host);
      const host = ref(null);
      const map = ref(null);

      host.value = hostRepo.all(); //
      const stationLayer = ref(null);

      const updateMarkers = async() => {
        if( map.value ){
          // function to update markers when the data changes
          console.log( "update markers" );
          stationLayer.value.clearLayers();
          features.value.map( (feature) => {
            let coords = feature.geometry.coordinates.reverse();
            const marker = L.marker(coords, {
              // Set the marker icon, if desired
              icon: L.icon({
                iconUrl: 'marker-icon.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
              }),
            });
            // set ID for marker
            marker.id = feature.id;
            // set type of marker
            marker.type = "host";
            // add popup to marker
            marker.bindPopup('<h3><a href="#/station/'+feature.id+'"/>' + feature.properties.name + '</a></h3>');
            stationLayer.value.addLayer(marker)
          })
          // geojsonLayer.value.addData( features.value );
        }
      };

      const onMapLoaded = async (mapInstance) => {
        map.value = mapInstance
        console.log("setting up map")
        stationLayer.value = L.markerClusterGroup().addTo(map.value)
        if( features.value.length ){
          updateMarkers()
        }
      };
      watch(features , () => {updateMarkers()});

    onMounted( () => {
      features.value = convertToGeoJson(host.value);
    });
      return {onMapLoaded};
    }
  });

  // the following to be moved to utils
  function convertToGeoJson(data) {
  const geoJsonData = data.map(d => {
    // extract the coordinates from WKT string and create a LatLng object
    const coords = d.location.match(/POINT\(([-\d\.]+)\s+([-\d\.]+)\)/);
    const latlng = [parseFloat(coords[1]), parseFloat(coords[2])];
    return {
      //type: 'FeatureCollection',
      //features: [{
        id: d.id,
        type: 'Feature',
        properties: {
          name: d.name,
          wigos_station_identifier: d.wigos_station_identifier,
          selected: false
          // add any additional properties here
        },
        geometry: {
          type: 'Point',
          coordinates: latlng
        },
      //}]
    };
  });
  return geoJsonData;
}

</script>
