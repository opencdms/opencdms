<template>
  <v-card>
    <v-card-title>Create new 'Feature'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="feature.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="feature.name"  hint="Name of feature" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="feature.description"  hint="Description of feature" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-select :items="featureTypeOptions" item-title="name" item-value="id" label="feature_type" v-model="feature.feature_type" :hint="featureTypeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="geometry" v-model="feature.geometry"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="elevation" v-model="feature.elevation" type="number" hint="Meam elevation of feature above mean sea level" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="featureOptions" item-title="name" item-value="id" label="feature" v-model="feature.parent" :hint="featureOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="properties" v-model="feature.properties"  hint="Array of named values consistent with that defined for the feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="feature._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="feature._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="feature._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="feature._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="feature.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createFeature">Create Feature</v-btn>
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


import FeatureType from '@/models/FeatureType';
import Feature from '@/models/Feature';
import User from '@/models/User';
import Status from '@/models/Status';

export default defineComponent({
  name: 'FeatureForm',
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
      feature.value.links = updatedLinks;
    }

    // set up repos
    const featureTypeRepo = useRepo(FeatureType);
    const featureTypeOptions = computed(() => { return featureTypeRepo.all() });
    const featureTypeOptionsHint = computed(() => {
      if( feature.value.feature_type !== null ){
        if ( 'description' in feature.value.feature_type ){
          return feature.value.feature_type.description;
        }else{
          return "";
        }
      }else{
        return "Select feature_type";
      }
    } );
    const featureRepo = useRepo(Feature);
    const featureOptions = computed(() => { return featureRepo.all() });
    const featureOptionsHint = computed(() => {
      if( feature.value.parent !== null ){
        if ( 'description' in feature.value.parent ){
          return feature.value.parent.description;
        }else{
          return "";
        }
      }else{
        return "Select feature";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( feature.value._user !== null ){
        if ( 'description' in feature.value._user ){
          return feature.value._user.description;
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
      if( feature.value._status !== null ){
        if ( 'description' in feature.value._status ){
          return feature.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const feature = ref(featureRepo.make());

    // function to create new object and to add to store
    const createFeature = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,feature.value);
        await featureRepo.save(valueToSave);
        resetFeature();
    };

    const resetFeature = () => {
        Object.assign(feature.value, featureRepo.make() );
    };

    return {
        feature,
        createFeature,
        resetFeature,
        links,
        updateLinks,
        featureTypeOptions, featureTypeOptionsHint,
        featureOptions, featureOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
