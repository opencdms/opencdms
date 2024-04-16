<template>
  <v-card>
    <v-card-title>Create new 'ControlSchedule'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="controlSchedule.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="controlSchedule.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="controlSchedule.description"  hint="Description of control schedule" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createControlSchedule">Create ControlSchedule</v-btn>
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
import ControlSchedule from '@/models/ControlSchedule';

export default defineComponent({
  name: 'ControlScheduleForm',
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
      controlSchedule.value.links = updatedLinks;
    }

    // set up repos

    const controlScheduleRepo = useRepo(ControlSchedule);
    const controlSchedule = ref(controlScheduleRepo.make());

    // function to create new object and to add to store
    const createControlSchedule = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,controlSchedule.value);
        await controlScheduleRepo.save(valueToSave);
        resetControlSchedule();
    };

    const resetControlSchedule = () => {
        Object.assign(controlSchedule.value, controlScheduleRepo.make() );
    };

    return {
        controlSchedule,
        createControlSchedule,
        resetControlSchedule,
        links,
        updateLinks
    }
  }
});
</script>
