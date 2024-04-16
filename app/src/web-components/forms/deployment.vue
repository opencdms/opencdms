<template>
  <v-card>
    <v-card-title>Create new 'Deployment'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="deployment.id"  hint="Unique ID / primary key for deployment" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="deployment.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observerOptions" item-title="name" item-value="id" label="observer" v-model="deployment.observer" :hint="observerOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="deployment.valid_from"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="deployment.valid_to"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="installation_height" v-model="deployment.installation_height" type="number" hint="Installation height above reference surface (in meters)" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="referenceSurfaceOptions" item-title="name" item-value="id" label="reference_surface" v-model="deployment.reference_surface" :hint="referenceSurfaceOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="exposureOptions" item-title="name" item-value="id" label="exposure" v-model="deployment.exposure" :hint="exposureOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="configuration" v-model="deployment.configuration"  hint="Textual description of sensor installation and configuration" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="maintenanceScheduleOptions" item-title="name" item-value="id" label="maintenance_schedule" v-model="deployment.maintenance_schedule" :hint="maintenanceScheduleOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="deployment._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="deployment._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="deployment._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="deployment._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="deployment.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createDeployment">Create Deployment</v-btn>
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


import Host from '@/models/Host';
import Observer from '@/models/Observer';
import ReferenceSurface from '@/models/ReferenceSurface';
import Exposure from '@/models/Exposure';
import MaintenanceSchedule from '@/models/MaintenanceSchedule';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Deployment from '@/models/Deployment';

export default defineComponent({
  name: 'DeploymentForm',
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
      deployment.value.links = updatedLinks;
    }

    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( deployment.value.host !== null ){
        if ( 'description' in deployment.value.host ){
          return deployment.value.host.description;
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
      if( deployment.value.observer !== null ){
        if ( 'description' in deployment.value.observer ){
          return deployment.value.observer.description;
        }else{
          return "";
        }
      }else{
        return "Select observer";
      }
    } );
    const referenceSurfaceRepo = useRepo(ReferenceSurface);
    const referenceSurfaceOptions = computed(() => { return referenceSurfaceRepo.all() });
    const referenceSurfaceOptionsHint = computed(() => {
      if( deployment.value.reference_surface !== null ){
        if ( 'description' in deployment.value.reference_surface ){
          return deployment.value.reference_surface.description;
        }else{
          return "";
        }
      }else{
        return "Select reference_surface";
      }
    } );
    const exposureRepo = useRepo(Exposure);
    const exposureOptions = computed(() => { return exposureRepo.all() });
    const exposureOptionsHint = computed(() => {
      if( deployment.value.exposure !== null ){
        if ( 'description' in deployment.value.exposure ){
          return deployment.value.exposure.description;
        }else{
          return "";
        }
      }else{
        return "Select exposure";
      }
    } );
    const maintenanceScheduleRepo = useRepo(MaintenanceSchedule);
    const maintenanceScheduleOptions = computed(() => { return maintenanceScheduleRepo.all() });
    const maintenanceScheduleOptionsHint = computed(() => {
      if( deployment.value.maintenance_schedule !== null ){
        if ( 'description' in deployment.value.maintenance_schedule ){
          return deployment.value.maintenance_schedule.description;
        }else{
          return "";
        }
      }else{
        return "Select maintenance_schedule";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( deployment.value._user !== null ){
        if ( 'description' in deployment.value._user ){
          return deployment.value._user.description;
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
      if( deployment.value._status !== null ){
        if ( 'description' in deployment.value._status ){
          return deployment.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const deploymentRepo = useRepo(Deployment);
    const deployment = ref(deploymentRepo.make());

    // function to create new object and to add to store
    const createDeployment = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,deployment.value);
        await deploymentRepo.save(valueToSave);
        resetDeployment();
    };

    const resetDeployment = () => {
        Object.assign(deployment.value, deploymentRepo.make() );
    };

    return {
        deployment,
        createDeployment,
        resetDeployment,
        links,
        updateLinks,
        hostOptions, hostOptionsHint,
        observerOptions, observerOptionsHint,
        referenceSurfaceOptions, referenceSurfaceOptionsHint,
        exposureOptions, exposureOptionsHint,
        maintenanceScheduleOptions, maintenanceScheduleOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
