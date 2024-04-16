<template>
  <v-card>
    <v-card-title>Create new 'SourceType'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="sourceType.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="sourceType.name"  hint="Name of source type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="sourceType.description"  hint="Description of source type, e.g. file etc" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="scheme" v-model="sourceType.scheme"  hint="IANA scheme (if applicable)" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="sourceType._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="sourceType._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="sourceType._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="sourceType._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="sourceType.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSourceType">Create SourceType</v-btn>
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
import SourceType from '@/models/SourceType';

export default defineComponent({
  name: 'SourceTypeForm',
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
      sourceType.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( sourceType.value._user !== null ){
        if ( 'description' in sourceType.value._user ){
          return sourceType.value._user.description;
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
      if( sourceType.value._status !== null ){
        if ( 'description' in sourceType.value._status ){
          return sourceType.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const sourceTypeRepo = useRepo(SourceType);
    const sourceType = ref(sourceTypeRepo.make());

    // function to create new object and to add to store
    const createSourceType = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,sourceType.value);
        await sourceTypeRepo.save(valueToSave);
        resetSourceType();
    };

    const resetSourceType = () => {
        Object.assign(sourceType.value, sourceTypeRepo.make() );
    };

    return {
        sourceType,
        createSourceType,
        resetSourceType,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
