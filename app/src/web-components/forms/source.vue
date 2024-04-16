<template>
  <v-card>
    <v-card-title>Create new 'Source'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="source.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="source.name"  hint="Name of source" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="source.description"  hint="Description of source type, e.g. file etc" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="sourceTypeOptions" item-title="name" item-value="id" label="source_type" v-model="source.source_type" :hint="sourceTypeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="processor" v-model="source.processor"  hint="Name of processor used to ingest the data" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="source._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="source._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="source._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="source._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="source.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSource">Create Source</v-btn>
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


import SourceType from '@/models/SourceType';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Source from '@/models/Source';

export default defineComponent({
  name: 'SourceForm',
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
      source.value.links = updatedLinks;
    }

    // set up repos
    const sourceTypeRepo = useRepo(SourceType);
    const sourceTypeOptions = computed(() => { return sourceTypeRepo.all() });
    const sourceTypeOptionsHint = computed(() => {
      if( source.value.source_type !== null ){
        if ( 'description' in source.value.source_type ){
          return source.value.source_type.description;
        }else{
          return "";
        }
      }else{
        return "Select source_type";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( source.value._user !== null ){
        if ( 'description' in source.value._user ){
          return source.value._user.description;
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
      if( source.value._status !== null ){
        if ( 'description' in source.value._status ){
          return source.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const sourceRepo = useRepo(Source);
    const source = ref(sourceRepo.make());

    // function to create new object and to add to store
    const createSource = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,source.value);
        await sourceRepo.save(valueToSave);
        resetSource();
    };

    const resetSource = () => {
        Object.assign(source.value, sourceRepo.make() );
    };

    return {
        source,
        createSource,
        resetSource,
        links,
        updateLinks,
        sourceTypeOptions, sourceTypeOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
