<template>
  <v-card>
    <v-card-title>Create new 'Observation'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observation.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="location" v-model="observation.location"  hint="Location of observation" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="elevation" v-model="observation.elevation" type="number" hint="Elevation of observation above mean sea level (in meters)" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="observationTypeOptions" item-title="name" item-value="id" label="observation_type" v-model="observation.observation_type" :hint="observationTypeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="phenomenon_start" v-model="observation.phenomenon_start"  hint="Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="phenomenon_end" v-model="observation.phenomenon_end"  hint="End time of the phenomenon being observed or observing period" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="result_value" v-model="observation.result_value" type="number" hint="The value of the result in float representation" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="result_uom" v-model="observation.result_uom"  hint="Units used to represent the value being observed" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="result_description" v-model="observation.result_description"  hint="str representation of the result if applicable" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="result_quality" v-model="observation.result_quality"  hint="JSON representation of the result quality, key / value pairs" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="result_time" v-model="observation.result_time"  hint="Time that the result became available" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="observation.valid_from"  hint="Time that the result starts to be valid" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="observation.valid_to"  hint="Time after which the result is no longer valid" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="observation.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observerOptions" item-title="name" item-value="id" label="observer" v-model="observation.observer" :hint="observerOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observedPropertyOptions" item-title="name" item-value="id" label="observed_property" v-model="observation.observed_property" :hint="observedPropertyOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observingProcedureOptions" item-title="name" item-value="id" label="observing_procedure" v-model="observation.observing_procedure" :hint="observingProcedureOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="collectionOptions" item-title="name" item-value="id" label="collection" v-model="observation.collection" :hint="collectionOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="parameter" v-model="observation.parameter"  hint="List of key/ value pairs in dict" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="featureOptions" item-title="name" item-value="id" label="feature" v-model="observation.feature" :hint="featureOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observation._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observation._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observation._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observation._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observation.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="sourceOptions" item-title="name" item-value="id" label="source" v-model="observation._source" :hint="sourceOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="_source_identifier" v-model="observation._source_identifier"  hint="The original identifier for the record from the data source" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObservation">Create Observation</v-btn>
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


import ObservationType from '@/models/ObservationType';
import Host from '@/models/Host';
import Observer from '@/models/Observer';
import ObservedProperty from '@/models/ObservedProperty';
import ObservingProcedure from '@/models/ObservingProcedure';
import Collection from '@/models/Collection';
import Feature from '@/models/Feature';
import User from '@/models/User';
import Status from '@/models/Status';
import Source from '@/models/Source';

// import model
import Observation from '@/models/Observation';

export default defineComponent({
  name: 'ObservationForm',
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
      observation.value.links = updatedLinks;
    }

    // set up repos
    const observationTypeRepo = useRepo(ObservationType);
    const observationTypeOptions = computed(() => { return observationTypeRepo.all() });
    const observationTypeOptionsHint = computed(() => {
      if( observation.value.observation_type !== null ){
        if ( 'description' in observation.value.observation_type ){
          return observation.value.observation_type.description;
        }else{
          return "";
        }
      }else{
        return "Select observation_type";
      }
    } );
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( observation.value.host !== null ){
        if ( 'description' in observation.value.host ){
          return observation.value.host.description;
        }else{
          return "";
        }
      }else{
        return "Select host";
      }
    } );
    const observerRepo = useRepo(Observer);
    const observerOptions = computed(() => { return observerRepo.all() });
    const observerOptionsHint = computed(() => {
      if( observation.value.observer !== null ){
        if ( 'description' in observation.value.observer ){
          return observation.value.observer.description;
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
      if( observation.value.observed_property !== null ){
        if ( 'description' in observation.value.observed_property ){
          return observation.value.observed_property.description;
        }else{
          return "";
        }
      }else{
        return "Select observed_property";
      }
    } );
    const observingProcedureRepo = useRepo(ObservingProcedure);
    const observingProcedureOptions = computed(() => { return observingProcedureRepo.all() });
    const observingProcedureOptionsHint = computed(() => {
      if( observation.value.observing_procedure !== null ){
        if ( 'description' in observation.value.observing_procedure ){
          return observation.value.observing_procedure.description;
        }else{
          return "";
        }
      }else{
        return "Select observing_procedure";
      }
    } );
    const collectionRepo = useRepo(Collection);
    const collectionOptions = computed(() => { return collectionRepo.all() });
    const collectionOptionsHint = computed(() => {
      if( observation.value.collection !== null ){
        if ( 'description' in observation.value.collection ){
          return observation.value.collection.description;
        }else{
          return "";
        }
      }else{
        return "Select collection";
      }
    } );
    const featureRepo = useRepo(Feature);
    const featureOptions = computed(() => { return featureRepo.all() });
    const featureOptionsHint = computed(() => {
      if( observation.value.feature !== null ){
        if ( 'description' in observation.value.feature ){
          return observation.value.feature.description;
        }else{
          return "";
        }
      }else{
        return "Select feature";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observation.value._user !== null ){
        if ( 'description' in observation.value._user ){
          return observation.value._user.description;
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
      if( observation.value._status !== null ){
        if ( 'description' in observation.value._status ){
          return observation.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );
    const sourceRepo = useRepo(Source);
    const sourceOptions = computed(() => { return sourceRepo.all() });
    const sourceOptionsHint = computed(() => {
      if( observation.value._source !== null ){
        if ( 'description' in observation.value._source ){
          return observation.value._source.description;
        }else{
          return "";
        }
      }else{
        return "Select source";
      }
    } );

    const observationRepo = useRepo(Observation);
    const observation = ref(observationRepo.make());

    // function to create new object and to add to store
    const createObservation = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observation.value);
        await observationRepo.save(valueToSave);
        resetObservation();
    };

    const resetObservation = () => {
        Object.assign(observation.value, observationRepo.make() );
    };

    return {
        observation,
        createObservation,
        resetObservation,
        links,
        updateLinks,
        observationTypeOptions, observationTypeOptionsHint,
        hostOptions, hostOptionsHint,
        observerOptions, observerOptionsHint,
        observedPropertyOptions, observedPropertyOptionsHint,
        observingProcedureOptions, observingProcedureOptionsHint,
        collectionOptions, collectionOptionsHint,
        featureOptions, featureOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint,
        sourceOptions, sourceOptionsHint
    }
  }
});
</script>
