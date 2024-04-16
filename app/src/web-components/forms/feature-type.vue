<template>
  <v-card>
    <v-card-title>Create new 'FeatureType'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="featureType.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="featureType.authority"  hint="Naming authority for code list entry" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="featureType.name"  hint="Short name for feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="featureType.description"  hint="Description of feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="featureType._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="featureType._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="featureType._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="featureType._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="featureType.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createFeatureType">Create FeatureType</v-btn>
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
import FeatureType from '@/models/FeatureType';

export default defineComponent({
  name: 'FeatureTypeForm',
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
      featureType.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( featureType.value._user !== null ){
        if ( 'description' in featureType.value._user ){
          return featureType.value._user.description;
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
      if( featureType.value._status !== null ){
        if ( 'description' in featureType.value._status ){
          return featureType.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const featureTypeRepo = useRepo(FeatureType);
    const featureType = ref(featureTypeRepo.make());

    // function to create new object and to add to store
    const createFeatureType = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,featureType.value);
        await featureTypeRepo.save(valueToSave);
        resetFeatureType();
    };

    const resetFeatureType = () => {
        Object.assign(featureType.value, featureTypeRepo.make() );
    };

    return {
        featureType,
        createFeatureType,
        resetFeatureType,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
