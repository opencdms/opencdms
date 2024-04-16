<template>
  <v-card>
    <v-card-title>Create new 'Observer'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observer.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="observer.name"  hint="Name of sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="observer.description"  hint="Description of sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="location" v-model="observer.location"  hint="Location of observer" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="elevation" v-model="observer.elevation" type="number" hint="Elevation of observer above mean sea level" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="manufacturer" v-model="observer.manufacturer"  hint="Make, or manufacturer, of sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="model" v-model="observer.model"  hint="Model of sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="serial_number" v-model="observer.serial_number"  hint="Serial number of sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="firmware_version" v-model="observer.firmware_version"  hint="Firmware version of software installed in sensor" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="controlScheduleOptions" item-title="name" item-value="id" label="control_schedule" v-model="observer.control_schedule" :hint="controlScheduleOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observer._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observer._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observer._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observer._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observer.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObserver">Create Observer</v-btn>
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


import ControlSchedule from '@/models/ControlSchedule';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Observer from '@/models/Observer';

export default defineComponent({
  name: 'ObserverForm',
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
      observer.value.links = updatedLinks;
    }

    // set up repos
    const controlScheduleRepo = useRepo(ControlSchedule);
    const controlScheduleOptions = computed(() => { return controlScheduleRepo.all() });
    const controlScheduleOptionsHint = computed(() => {
      if( observer.value.control_schedule !== null ){
        if ( 'description' in observer.value.control_schedule ){
          return observer.value.control_schedule.description;
        }else{
          return "";
        }
      }else{
        return "Select control_schedule";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observer.value._user !== null ){
        if ( 'description' in observer.value._user ){
          return observer.value._user.description;
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
      if( observer.value._status !== null ){
        if ( 'description' in observer.value._status ){
          return observer.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observerRepo = useRepo(Observer);
    const observer = ref(observerRepo.make());

    // function to create new object and to add to store
    const createObserver = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observer.value);
        await observerRepo.save(valueToSave);
        resetObserver();
    };

    const resetObserver = () => {
        Object.assign(observer.value, observerRepo.make() );
    };

    return {
        observer,
        createObserver,
        resetObserver,
        links,
        updateLinks,
        controlScheduleOptions, controlScheduleOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
