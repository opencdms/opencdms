<template>
  <v-card>
    <v-card-title>Create new 'Territory'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="territory.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="ISO3c" v-model="territory.ISO3c"  hint="ISO 3 character country code" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="territory.name"  hint="Short name for feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="territory.description"  hint="Description of feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="wmoRegionOptions" item-title="name" item-value="id" label="wmo_region" v-model="territory.wmo_region" :hint="wmoRegionOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="territory._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="territory._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="territory._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="territory._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="territory.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createTerritory">Create Territory</v-btn>
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


import WmoRegion from '@/models/WmoRegion';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Territory from '@/models/Territory';

export default defineComponent({
  name: 'TerritoryForm',
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
      territory.value.links = updatedLinks;
    }

    // set up repos
    const wmoRegionRepo = useRepo(WmoRegion);
    const wmoRegionOptions = computed(() => { return wmoRegionRepo.all() });
    const wmoRegionOptionsHint = computed(() => {
      if( territory.value.wmo_region !== null ){
        if ( 'description' in territory.value.wmo_region ){
          return territory.value.wmo_region.description;
        }else{
          return "";
        }
      }else{
        return "Select wmo_region";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( territory.value._user !== null ){
        if ( 'description' in territory.value._user ){
          return territory.value._user.description;
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
      if( territory.value._status !== null ){
        if ( 'description' in territory.value._status ){
          return territory.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const territoryRepo = useRepo(Territory);
    const territory = ref(territoryRepo.make());

    // function to create new object and to add to store
    const createTerritory = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,territory.value);
        await territoryRepo.save(valueToSave);
        resetTerritory();
    };

    const resetTerritory = () => {
        Object.assign(territory.value, territoryRepo.make() );
    };

    return {
        territory,
        createTerritory,
        resetTerritory,
        links,
        updateLinks,
        wmoRegionOptions, wmoRegionOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
