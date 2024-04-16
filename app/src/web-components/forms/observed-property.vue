<template>
  <v-card>
    <v-card-title>Create new 'ObservedProperty'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observedProperty.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="observedProperty.authority"  hint="Naming authority for code list entry" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="short_name" v-model="observedProperty.short_name"  hint="Short name representation of observed property, e.g. 'at' for air temperature" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="standard_name" v-model="observedProperty.standard_name"  hint="CF standard name (if applicable), e.g. 'air_temperature'" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="units" v-model="observedProperty.units"  hint="Canonical units, e.g. 'Kelvin'" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="observedProperty.description"  hint="Description of observed property" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observedProperty._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observedProperty._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observedProperty._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observedProperty._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observedProperty.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObservedProperty">Create ObservedProperty</v-btn>
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
import ObservedProperty from '@/models/ObservedProperty';

export default defineComponent({
  name: 'ObservedPropertyForm',
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
      observedProperty.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observedProperty.value._user !== null ){
        if ( 'description' in observedProperty.value._user ){
          return observedProperty.value._user.description;
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
      if( observedProperty.value._status !== null ){
        if ( 'description' in observedProperty.value._status ){
          return observedProperty.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observedPropertyRepo = useRepo(ObservedProperty);
    const observedProperty = ref(observedPropertyRepo.make());

    // function to create new object and to add to store
    const createObservedProperty = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observedProperty.value);
        await observedPropertyRepo.save(valueToSave);
        resetObservedProperty();
    };

    const resetObservedProperty = () => {
        Object.assign(observedProperty.value, observedPropertyRepo.make() );
    };

    return {
        observedProperty,
        createObservedProperty,
        resetObservedProperty,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
