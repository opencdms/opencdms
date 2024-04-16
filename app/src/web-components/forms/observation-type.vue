<template>
  <v-card>
    <v-card-title>Create new 'ObservationType'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observationType.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="observationType.authority"  hint="naming authority for code list entry" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="observationType.name"  hint="Short name for observation type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="observationType.description"  hint="Description of observation type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observationType._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observationType._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observationType._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observationType._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observationType.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObservationType">Create ObservationType</v-btn>
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


import User from '@/models/User';
import Status from '@/models/Status';

// import model
import ObservationType from '@/models/ObservationType';

export default defineComponent({
  name: 'ObservationTypeForm',
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
      observationType.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observationType.value._user !== null ){
        if ( 'description' in observationType.value._user ){
          return observationType.value._user.description;
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
      if( observationType.value._status !== null ){
        if ( 'description' in observationType.value._status ){
          return observationType.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observationTypeRepo = useRepo(ObservationType);
    const observationType = ref(observationTypeRepo.make());

    // function to create new object and to add to store
    const createObservationType = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observationType.value);
        await observationTypeRepo.save(valueToSave);
        resetObservationType();
    };

    const resetObservationType = () => {
        Object.assign(observationType.value, observationTypeRepo.make() );
    };

    return {
        observationType,
        createObservationType,
        resetObservationType,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
