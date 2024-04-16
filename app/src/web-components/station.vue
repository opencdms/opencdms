<template>
  <v-container>
    <v-row>
    <v-col :cols="12">
      <v-card>
        <v-card-title>Select station</v-card-title>
        <v-card-text><select-host v-model="selectedHost"/></v-card-text>
      </v-card>
    </v-col>
    </v-row>
    <v-row>
    </v-row>
    <v-row v-if="host != null">
      <v-col :cols="6">
        <v-card>
          <v-card-title>
            Station: {{ $route.params.id }}
          </v-card-title>
          <v-card-item><v-card-text><pre>{{host}}</pre></v-card-text></v-card-item>
        </v-card>
      </v-col>
      <v-col :cols="6" align-self="center">
        <feature-map :geom="geom" id="map" style="height: 500px;"/>
      </v-col>
    </v-row>
    <v-row>
      <v-col :cols="12">
        <v-btn @click="edit">Edit</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { defineComponent, ref, watchEffect, computed, watch } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VTabs, VTab, VBtn, VAutocomplete } from 'vuetify/lib/components';
import { VContainer, VCol, VRow } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import { useRoute, useRouter } from 'vue-router';

import {useRepo} from 'pinia-orm';

import FeatureMap from '@/web-components/maps/feature-map.vue'

import SelectHost from '@/web-components/pickers/select-host.vue';


// opencdms imports
import Host from '@/models/Host';

export default defineComponent({
  name: 'station',
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    VTabs,
    VTab,
    VBtn,
    VAutocomplete, VContainer, VCol, VRow,
    FeatureMap,
    SelectHost
  },
  methods: {},
  setup(props) {
    // set up varaiables
    const selectedHost = ref(null)
    const router = useRouter();
    const geom = ref(null);
    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const host = ref(null)

    const edit = () => {
      router.push('/station/'+route.params.id+'/edit');
    };

    const fetchRecord = async(identifier) => {
      // load selected host
      var host_tmp = useRepo(Host).where('id',route.params.id).first();
      if ( host_tmp != null ){
        host.value = host_tmp;
      }
      console.log(host.value);
    }

    // add watch to update the geom
    watch(host, (newVal) => {
      if( newVal ){
        const coords = newVal.location.match(/POINT\(([-\d\.]+)\s+([-\d\.]+)\)/);
        const latlng = [parseFloat(coords[1]), parseFloat(coords[2])];
        geom.value = {
          type: 'Feature',
          geometry: {
            type: 'Point',
            coordinates: latlng
          }
        }
      }
      console.log(geom.value)
    });

    const route = useRoute();
    const data = ref([]);


    onMounted( async() => {
      fetchRecord( route.params.id );
      watchEffect( () => {
        fetchRecord( route.params.id );
      });
      watch( (selectedHost), (data) => {
        router.push('/station/'+data.id);
      } )
    });
    onErrorCaptured( () => {});
    return {host, edit, hostOptions, selectedHost, geom};
  }

});
</script>
