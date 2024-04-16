<template>
  <v-card>
    <v-card-title>Create new 'ObserverResponsibleParty'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observerResponsibleParty.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="responsiblePartyOptions" item-title="name" item-value="id" label="responsible_party" v-model="observerResponsibleParty.responsible_party" :hint="responsiblePartyOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="roleOptions" item-title="name" item-value="id" label="role" v-model="observerResponsibleParty.role" :hint="roleOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="observerOptions" item-title="name" item-value="id" label="observer" v-model="observerResponsibleParty.observer" :hint="observerOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="observerResponsibleParty.valid_from"  hint="Date this record is valid from" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="observerResponsibleParty.valid_to"  hint="Date this record is valid to" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observerResponsibleParty._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observerResponsibleParty._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observerResponsibleParty._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observerResponsibleParty._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observerResponsibleParty.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObserverResponsibleParty">Create ObserverResponsibleParty</v-btn>
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


import ResponsibleParty from '@/models/ResponsibleParty';
import Role from '@/models/Role';
import Observer from '@/models/Observer';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import ObserverResponsibleParty from '@/models/ObserverResponsibleParty';

export default defineComponent({
  name: 'ObserverResponsiblePartyForm',
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
      observerResponsibleParty.value.links = updatedLinks;
    }

    // set up repos
    const responsiblePartyRepo = useRepo(ResponsibleParty);
    const responsiblePartyOptions = computed(() => { return responsiblePartyRepo.all() });
    const responsiblePartyOptionsHint = computed(() => {
      if( observerResponsibleParty.value.responsible_party !== null ){
        if ( 'description' in observerResponsibleParty.value.responsible_party ){
          return observerResponsibleParty.value.responsible_party.description;
        }else{
          return "";
        }
      }else{
        return "Select responsible_party";
      }
    } );
    const roleRepo = useRepo(Role);
    const roleOptions = computed(() => { return roleRepo.all() });
    const roleOptionsHint = computed(() => {
      if( observerResponsibleParty.value.role !== null ){
        if ( 'description' in observerResponsibleParty.value.role ){
          return observerResponsibleParty.value.role.description;
        }else{
          return "";
        }
      }else{
        return "Select role";
      }
    } );
    const observerRepo = useRepo(Observer);
    const observerOptions = computed(() => { return observerRepo.all() });
    const observerOptionsHint = computed(() => {
      if( observerResponsibleParty.value.observer !== null ){
        if ( 'description' in observerResponsibleParty.value.observer ){
          return observerResponsibleParty.value.observer.description;
        }else{
          return "";
        }
      }else{
        return "Select observer";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observerResponsibleParty.value._user !== null ){
        if ( 'description' in observerResponsibleParty.value._user ){
          return observerResponsibleParty.value._user.description;
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
      if( observerResponsibleParty.value._status !== null ){
        if ( 'description' in observerResponsibleParty.value._status ){
          return observerResponsibleParty.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observerResponsiblePartyRepo = useRepo(ObserverResponsibleParty);
    const observerResponsibleParty = ref(observerResponsiblePartyRepo.make());

    // function to create new object and to add to store
    const createObserverResponsibleParty = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observerResponsibleParty.value);
        await observerResponsiblePartyRepo.save(valueToSave);
        resetObserverResponsibleParty();
    };

    const resetObserverResponsibleParty = () => {
        Object.assign(observerResponsibleParty.value, observerResponsiblePartyRepo.make() );
    };

    return {
        observerResponsibleParty,
        createObserverResponsibleParty,
        resetObserverResponsibleParty,
        links,
        updateLinks,
        responsiblePartyOptions, responsiblePartyOptionsHint,
        roleOptions, roleOptionsHint,
        observerOptions, observerOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
