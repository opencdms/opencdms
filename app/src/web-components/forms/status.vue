<template>
  <v-card>
    <v-card-title>Create new 'Status'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="status.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="status.name"  hint="Short name for status" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="status.description"  hint="Description of the status" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createStatus">Create Status</v-btn>
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
import Status from '@/models/Status';

export default defineComponent({
  name: 'StatusForm',
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
      status.value.links = updatedLinks;
    }

    // set up repos

    const statusRepo = useRepo(Status);
    const status = ref(statusRepo.make());

    // function to create new object and to add to store
    const createStatus = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,status.value);
        await statusRepo.save(valueToSave);
        resetStatus();
    };

    const resetStatus = () => {
        Object.assign(status.value, statusRepo.make() );
    };

    return {
        status,
        createStatus,
        resetStatus,
        links,
        updateLinks
    }
  }
});
</script>
