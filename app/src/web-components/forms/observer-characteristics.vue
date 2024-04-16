<template>
  <v-card>
    <v-card-title>Create new 'ObserverCharacteristics'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observerCharacteristics.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="observerOptions" item-title="name" item-value="id" label="observer" v-model="observerCharacteristics.observer" :hint="observerOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observedPropertyOptions" item-title="name" item-value="id" label="observed_property" v-model="observerCharacteristics.observed_property" :hint="observedPropertyOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observingMethodOptions" item-title="name" item-value="id" label="observing_method" v-model="observerCharacteristics.observing_method" :hint="observingMethodOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="measurement_units" v-model="observerCharacteristics.measurement_units" type="number" hint="The units used in this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="drift_per_unit_time" v-model="observerCharacteristics.drift_per_unit_time" type="number" hint="Sensor drift per unit time, units specified by measurement units, unit time by unit time" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="unit_time" v-model="observerCharacteristics.unit_time" type="number" hint="Unit time for drift per unit time (seconds)" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="valid_min" v-model="observerCharacteristics.valid_min" type="number" hint="Minimum observable value by sensor, in units specificed by measurement units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="valid_max" v-model="observerCharacteristics.valid_max" type="number" hint="Maximum observable value by sensor, in units specificed by measurement units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="measurement_uncertainty" v-model="observerCharacteristics.measurement_uncertainty" type="number" hint="Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measuremenet units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="measurement_accuracy" v-model="observerCharacteristics.measurement_accuracy" type="number" hint="Measurement accuracy (trueness) for measurements from this sensor, 2 sigma. Units as per measuremenet units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="measurement_repeatability" v-model="observerCharacteristics.measurement_repeatability" type="number" hint="Measurement repeatability (precision) for measurements from this sensor, 2 sigma. Units as per measuremenet units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="measurement_resolution" v-model="observerCharacteristics.measurement_resolution" type="number" hint="Minimum change detectable for measurements from this sensor. Units as per measurement units" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observerCharacteristics._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observerCharacteristics._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observerCharacteristics._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observerCharacteristics._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observerCharacteristics.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObserverCharacteristics">Create ObserverCharacteristics</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
import * as d3 from 'd3';
import { defineComponent, ref, computed } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VForm, VTextField, VSelect, VBtn } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import {useStore} from 'pinia';
import {useRepo} from 'pinia-orm';

import LinkForm from '@/web-components/forms/links';
import VueDatePicker from '@/web-components/pickers/date-picker.vue';


import Observer from '@/models/Observer';
import ObservedProperty from '@/models/ObservedProperty';
import ObservingMethod from '@/models/ObservingMethod';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import ObserverCharacteristics from '@/models/ObserverCharacteristics';

export default defineComponent({
  name: 'ObserverCharacteristicsForm',
  props: {
  },
  methods:{
    parseLinks (links) {
      let res;
      if( links && links.length > 0 ){
        res = JSON.stringify(links);
      }else{
        res = '';
      }
      return res;
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    VTextField,
    VSelect,
    VForm,
    VBtn,
    VueDatePicker,
    LinkForm
  },
  setup() {

    // set up links object
    const links = ref([]);
    const updateLinks = (updatedLinks) => {
      console.log("updating links");
      observerCharacteristics.value.links = updatedLinks;
    }

    // set up repos
    const observerRepo = useRepo(Observer);
    const observerOptions = computed(() => { return observerRepo.all() });
    const observerOptionsHint = computed(() => {
      if( observerCharacteristics.value.observer !== null ){
        if ( 'description' in observerCharacteristics.value.observer ){
          return observerCharacteristics.value.observer.description;
        }else{
          return "";
        }
      }else{
        return "Select observer";
      }
    } );
    const observedPropertyRepo = useRepo(ObservedProperty);
    const observedPropertyOptions = computed(() => { return observedPropertyRepo.all() });
    const observedPropertyOptionsHint = computed(() => {
      if( observerCharacteristics.value.observed_property !== null ){
        if ( 'description' in observerCharacteristics.value.observed_property ){
          return observerCharacteristics.value.observed_property.description;
        }else{
          return "";
        }
      }else{
        return "Select observed_property";
      }
    } );
    const observingMethodRepo = useRepo(ObservingMethod);
    const observingMethodOptions = computed(() => { return observingMethodRepo.all() });
    const observingMethodOptionsHint = computed(() => {
      if( observerCharacteristics.value.observing_method !== null ){
        if ( 'description' in observerCharacteristics.value.observing_method ){
          return observerCharacteristics.value.observing_method.description;
        }else{
          return "";
        }
      }else{
        return "Select observing_method";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observerCharacteristics.value._user !== null ){
        if ( 'description' in observerCharacteristics.value._user ){
          return observerCharacteristics.value._user.description;
        }else{
          return "";
        }
      }else{
        return "Select user";
      }
    } );
    const statusRepo = useRepo(Status);
    const statusOptions = computed(() => { return statusRepo.all() });
    const statusOptionsHint = computed(() => {
      if( observerCharacteristics.value._status !== null ){
        if ( 'description' in observerCharacteristics.value._status ){
          return observerCharacteristics.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observerCharacteristicsRepo = useRepo(ObserverCharacteristics);
    const observerCharacteristics = ref(observerCharacteristicsRepo.make());

    // function to create new object and to add to store
    const createObserverCharacteristics = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observerCharacteristics.value);
        await observerCharacteristicsRepo.save(valueToSave);
        resetObserverCharacteristics();
    };

    const resetObserverCharacteristics = () => {
        Object.assign(observerCharacteristics.value, observerCharacteristicsRepo.make() );
    };

    return {
        observerCharacteristics,
        createObserverCharacteristics,
        resetObserverCharacteristics,
        links,
        updateLinks,
        observerOptions, observerOptionsHint,
        observedPropertyOptions, observedPropertyOptionsHint,
        observingMethodOptions, observingMethodOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
