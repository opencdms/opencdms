<template>
  <v-container>
    <v-row>
    <v-col :cols="12">
      <v-card>
        <v-card-title>Select sensor</v-card-title>
        <v-card-text><select-observer v-model="selectedObserver"/></v-card-text>
      </v-card>
    </v-col>
    </v-row>
    <v-row>
    </v-row>
    <v-row>
      <v-col :cols="6">
        <v-card>
          <v-card-title>Sensor: {{ $route.params.id }}</v-card-title>
            <v-card-item><v-card-text><pre>{{observer}}</pre></v-card-text></v-card-item>
        </v-card>
      </v-col>
      <v-col :cols="6" align-self="center">
        <feature-map :geom="geom" id="map" style="height: 400px;"/>
      </v-col>
    </v-row>
    <v-row>
      <v-col :cols="12">
        <v-card>
          <v-card-title>Sensor characteristics</v-card-title>
            <v-card-item><v-card-text><pre>{{observerCharacteristics}}</pre></v-card-text></v-card-item>
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

import SelectObserver from '@/web-components/pickers/select-observer.vue';


// opencdms imports
import Observer from '@/models/Observer';
import ObserverCharacteristics from '@/models/ObserverCharacteristics';

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
    SelectObserver
  },
  methods: {},
  setup(props) {
    // set up varaiables
    const selectedObserver = ref(null)
    const router = useRouter();
    const geom = ref(null);
    // set up repos
    const observerRepo = useRepo(Observer);
    const observerOptions = computed(() => { return observerRepo.all() });
    const observer = ref(null)
    const observerCharacteristics = ref(null)

    const edit = () => {
      router.push('/sensor/'+route.params.id+'/edit');
    };

    const fetchRecord = async(identifier) => {
      // load selected observer
      console.log(identifier);
      observer.value = useRepo(Observer).where('id',route.params.id).first();
      console.log(useRepo(Observer).all())
      // load observer characteristics
      observerCharacteristics.value = useRepo(ObserverCharacteristics).with('observed_property').with('observing_method').where('observer_id',route.params.id).first();
    }

    // add watch to update the geom
    watch(observer, (newVal) => {
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
      watch( (selectedObserver), (data) => {
        router.push('/sensor/'+data.id);
      } )
    });
    onErrorCaptured( () => {});
    return {observer, observerCharacteristics, observerOptions, selectedObserver, geom};
  }

});
</script>
