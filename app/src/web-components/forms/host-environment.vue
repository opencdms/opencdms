<template>
  <v-card>
    <v-card-title>Create new 'HostEnvironment'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="hostEnvironment.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="host" v-model="hostEnvironment.host"  hint="Host associated with this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="climateZoneOptions" item-title="name" item-value="id" label="climate_zone" v-model="hostEnvironment.climate_zone" :hint="climateZoneOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="surfaceCoverOptions" item-title="name" item-value="id" label="surface_cover" v-model="hostEnvironment.surface_cover" :hint="surfaceCoverOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="surfaceRoughnessOptions" item-title="name" item-value="id" label="surface_roughness" v-model="hostEnvironment.surface_roughness" :hint="surfaceRoughnessOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="topographyOptions" item-title="name" item-value="id" label="topography" v-model="hostEnvironment.topography" :hint="topographyOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="seasonOptions" item-title="name" item-value="id" label="season" v-model="hostEnvironment.season" :hint="seasonOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="hostEnvironment.valid_from"  hint="Date the this record is valid from" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="hostEnvironment.valid_to"  hint="date that this record is valid to" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="hostEnvironment._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="hostEnvironment._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="hostEnvironment._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="hostEnvironment._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="hostEnvironment.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHostEnvironment">Create HostEnvironment</v-btn>
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


import ClimateZone from '@/models/ClimateZone';
import SurfaceCover from '@/models/SurfaceCover';
import SurfaceRoughness from '@/models/SurfaceRoughness';
import Topography from '@/models/Topography';
import Season from '@/models/Season';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import HostEnvironment from '@/models/HostEnvironment';

export default defineComponent({
  name: 'HostEnvironmentForm',
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
      hostEnvironment.value.links = updatedLinks;
    }

    // set up repos
    const climateZoneRepo = useRepo(ClimateZone);
    const climateZoneOptions = computed(() => { return climateZoneRepo.all() });
    const climateZoneOptionsHint = computed(() => {
      if( hostEnvironment.value.climate_zone !== null ){
        if ( 'description' in hostEnvironment.value.climate_zone ){
          return hostEnvironment.value.climate_zone.description;
        }else{
          return "";
        }
      }else{
        return "Select climate_zone";
      }
    } );
    const surfaceCoverRepo = useRepo(SurfaceCover);
    const surfaceCoverOptions = computed(() => { return surfaceCoverRepo.all() });
    const surfaceCoverOptionsHint = computed(() => {
      if( hostEnvironment.value.surface_cover !== null ){
        if ( 'description' in hostEnvironment.value.surface_cover ){
          return hostEnvironment.value.surface_cover.description;
        }else{
          return "";
        }
      }else{
        return "Select surface_cover";
      }
    } );
    const surfaceRoughnessRepo = useRepo(SurfaceRoughness);
    const surfaceRoughnessOptions = computed(() => { return surfaceRoughnessRepo.all() });
    const surfaceRoughnessOptionsHint = computed(() => {
      if( hostEnvironment.value.surface_roughness !== null ){
        if ( 'description' in hostEnvironment.value.surface_roughness ){
          return hostEnvironment.value.surface_roughness.description;
        }else{
          return "";
        }
      }else{
        return "Select surface_roughness";
      }
    } );
    const topographyRepo = useRepo(Topography);
    const topographyOptions = computed(() => { return topographyRepo.all() });
    const topographyOptionsHint = computed(() => {
      if( hostEnvironment.value.topography !== null ){
        if ( 'description' in hostEnvironment.value.topography ){
          return hostEnvironment.value.topography.description;
        }else{
          return "";
        }
      }else{
        return "Select topography";
      }
    } );
    const seasonRepo = useRepo(Season);
    const seasonOptions = computed(() => { return seasonRepo.all() });
    const seasonOptionsHint = computed(() => {
      if( hostEnvironment.value.season !== null ){
        if ( 'description' in hostEnvironment.value.season ){
          return hostEnvironment.value.season.description;
        }else{
          return "";
        }
      }else{
        return "Select season";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( hostEnvironment.value._user !== null ){
        if ( 'description' in hostEnvironment.value._user ){
          return hostEnvironment.value._user.description;
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
      if( hostEnvironment.value._status !== null ){
        if ( 'description' in hostEnvironment.value._status ){
          return hostEnvironment.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostEnvironmentRepo = useRepo(HostEnvironment);
    const hostEnvironment = ref(hostEnvironmentRepo.make());

    // function to create new object and to add to store
    const createHostEnvironment = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,hostEnvironment.value);
        await hostEnvironmentRepo.save(valueToSave);
        resetHostEnvironment();
    };

    const resetHostEnvironment = () => {
        Object.assign(hostEnvironment.value, hostEnvironmentRepo.make() );
    };

    return {
        hostEnvironment,
        createHostEnvironment,
        resetHostEnvironment,
        links,
        updateLinks,
        climateZoneOptions, climateZoneOptionsHint,
        surfaceCoverOptions, surfaceCoverOptionsHint,
        surfaceRoughnessOptions, surfaceRoughnessOptionsHint,
        topographyOptions, topographyOptionsHint,
        seasonOptions, seasonOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
