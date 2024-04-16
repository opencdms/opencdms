<template>
  <v-card>
    <v-card-title>Create new 'MaintenanceSchedule'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="maintenanceSchedule.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="maintenanceSchedule.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="maintenanceSchedule.description"  hint="Description of maintenance schedule" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createMaintenanceSchedule">Create MaintenanceSchedule</v-btn>
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



// import model
import MaintenanceSchedule from '@/models/MaintenanceSchedule';

export default defineComponent({
  name: 'MaintenanceScheduleForm',
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
      maintenanceSchedule.value.links = updatedLinks;
    }

    // set up repos

    const maintenanceScheduleRepo = useRepo(MaintenanceSchedule);
    const maintenanceSchedule = ref(maintenanceScheduleRepo.make());

    // function to create new object and to add to store
    const createMaintenanceSchedule = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,maintenanceSchedule.value);
        await maintenanceScheduleRepo.save(valueToSave);
        resetMaintenanceSchedule();
    };

    const resetMaintenanceSchedule = () => {
        Object.assign(maintenanceSchedule.value, maintenanceScheduleRepo.make() );
    };

    return {
        maintenanceSchedule,
        createMaintenanceSchedule,
        resetMaintenanceSchedule,
        links,
        updateLinks
    }
  }
});
</script>
