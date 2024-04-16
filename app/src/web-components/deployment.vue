<template>
  <v-container>
    <v-row>
    <v-col :cols="12">
      <v-card>
        <v-card-title>Select deployment</v-card-title>
        <v-card-text><select-deployment v-model="selectedDeployment"/></v-card-text>
      </v-card>
    </v-col>
    <!-- </v-row>
    <v-row> -->
      <v-col :cols="6">
        <v-card>
          <v-card-title>Deployment: {{ $route.params.id }}</v-card-title>
          <v-card-text><pre>{{deployment}}</pre></v-card-text>
        </v-card>
        <v-card>
          <v-card-title>Associated station</v-card-title>
          <v-card-text><pre>{{host}}</pre></v-card-text>
        </v-card>
      </v-col>
      <v-col :cols="6" align-self="center">
        <feature-map :geom="geom" id="map" style="height: 400px;"/>
        <v-card>
          <v-card-title>Associated sensor</v-card-title>
          <v-card-text><pre>{{sensor}}</pre></v-card-text>
        </v-card>
        <v-card>
          <v-card-title>Sensor characteristic</v-card-title>
          <v-card-text><pre>{{sensorCharacteristics}}</pre></v-card-text>
        </v-card>
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

import SelectDeployment from '@/web-components/pickers/select-deployment.vue';
import ObserverCharacteristics from '@/models/ObserverCharacteristics';


// opencdms imports
import Deployment from '@/models/Deployment';
import Host from '@/models/Deployment';
import Observer from '@/models/Observer';

export default defineComponent({
  name: 'sensor',
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
    SelectDeployment
  },
  methods: {},
  setup(props) {
    // set up varaiables
    const selectedDeployment = ref(null)
    const router = useRouter();
    const geom = ref(null);
    // set up repos
    const deploymentRepo = useRepo(Deployment);
    const deploymentOptions = computed(() => { return deploymentRepo.all() });
    const deployment = ref(null)
    const host = ref(null)
    const sensor = ref(null)
    const sensorCharacteristics = ref(null)

    // const deploymentCharacteristics = ref(null)

    const edit = () => {
      router.push('/deployment/'+route.params.id+'/edit');
    };

    const fetchRecord = async(identifier) => {
      // load selected deployment
      deployment.value = await useRepo(Deployment).with('host').with('observer').where('id',route.params.id).first();
    }

    watch( deployment, () => {
      if( deployment.value ){
        var host_id = deployment.value.host_id;
        var observer_id = deployment.value.observer_id;
        host.value = deployment.value.host;
        sensor.value = useRepo(Observer).where('id', observer_id).first();
        console.log(deployment.value);
        sensorCharacteristics.value = useRepo(ObserverCharacteristics).with('observed_property').where('observer_id',observer_id).first();
        //delete deployment.value.host;
        //delete deployment.value.observer;
      }
    });


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
      watch( (selectedDeployment), (data) => {
        router.push('/deployment/'+data.id);
      } )
    });
    onErrorCaptured( () => {});
    return {deployment, host, sensor, sensorCharacteristics, deploymentOptions, selectedDeployment, geom};
  }

});
</script>
