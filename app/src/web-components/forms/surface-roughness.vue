<template>
  <v-card>
    <v-card-title>Create new 'SurfaceRoughness'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="surfaceRoughness.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="surfaceRoughness.authority"  hint="Naming authority for code list entry" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="surfaceRoughness.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="surfaceRoughness.description"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="surfaceRoughness._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="surfaceRoughness._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="surfaceRoughness._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="surfaceRoughness._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="surfaceRoughness.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSurfaceRoughness">Create SurfaceRoughness</v-btn>
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
import SurfaceRoughness from '@/models/SurfaceRoughness';

export default defineComponent({
  name: 'SurfaceRoughnessForm',
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
      surfaceRoughness.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( surfaceRoughness.value._user !== null ){
        if ( 'description' in surfaceRoughness.value._user ){
          return surfaceRoughness.value._user.description;
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
      if( surfaceRoughness.value._status !== null ){
        if ( 'description' in surfaceRoughness.value._status ){
          return surfaceRoughness.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const surfaceRoughnessRepo = useRepo(SurfaceRoughness);
    const surfaceRoughness = ref(surfaceRoughnessRepo.make());

    // function to create new object and to add to store
    const createSurfaceRoughness = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,surfaceRoughness.value);
        await surfaceRoughnessRepo.save(valueToSave);
        resetSurfaceRoughness();
    };

    const resetSurfaceRoughness = () => {
        Object.assign(surfaceRoughness.value, surfaceRoughnessRepo.make() );
    };

    return {
        surfaceRoughness,
        createSurfaceRoughness,
        resetSurfaceRoughness,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
