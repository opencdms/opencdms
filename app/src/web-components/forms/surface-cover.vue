<template>
  <v-card>
    <v-card-title>Create new 'SurfaceCover'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="surfaceCover.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="surfaceCover.authority"  hint="Naming authority for code list entry" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="surfaceCover.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="surfaceCover.description"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="surfaceCover._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="surfaceCover._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="surfaceCover._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="surfaceCover._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="surfaceCover.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSurfaceCover">Create SurfaceCover</v-btn>
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
import SurfaceCover from '@/models/SurfaceCover';

export default defineComponent({
  name: 'SurfaceCoverForm',
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
      surfaceCover.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( surfaceCover.value._user !== null ){
        if ( 'description' in surfaceCover.value._user ){
          return surfaceCover.value._user.description;
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
      if( surfaceCover.value._status !== null ){
        if ( 'description' in surfaceCover.value._status ){
          return surfaceCover.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const surfaceCoverRepo = useRepo(SurfaceCover);
    const surfaceCover = ref(surfaceCoverRepo.make());

    // function to create new object and to add to store
    const createSurfaceCover = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,surfaceCover.value);
        await surfaceCoverRepo.save(valueToSave);
        resetSurfaceCover();
    };

    const resetSurfaceCover = () => {
        Object.assign(surfaceCover.value, surfaceCoverRepo.make() );
    };

    return {
        surfaceCover,
        createSurfaceCover,
        resetSurfaceCover,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
