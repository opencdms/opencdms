<template>
  <v-card>
    <v-card-title>Create new 'HostResponsibleParty'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="hostResponsibleParty.id"  hint="Unique identifier for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="responsiblePartyOptions" item-title="name" item-value="id" label="responsible_party" v-model="hostResponsibleParty.responsible_party" :hint="responsiblePartyOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="roleOptions" item-title="name" item-value="id" label="role" v-model="hostResponsibleParty.role" :hint="roleOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="hostResponsibleParty.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="hostResponsibleParty.valid_from"  hint="Date this record is valid from" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="hostResponsibleParty.valid_to"  hint="Date this record is valid to" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="hostResponsibleParty._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="hostResponsibleParty._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="hostResponsibleParty._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="hostResponsibleParty._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="hostResponsibleParty.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHostResponsibleParty">Create HostResponsibleParty</v-btn>
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
import Host from '@/models/Host';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import HostResponsibleParty from '@/models/HostResponsibleParty';

export default defineComponent({
  name: 'HostResponsiblePartyForm',
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
      hostResponsibleParty.value.links = updatedLinks;
    }

    // set up repos
    const responsiblePartyRepo = useRepo(ResponsibleParty);
    const responsiblePartyOptions = computed(() => { return responsiblePartyRepo.all() });
    const responsiblePartyOptionsHint = computed(() => {
      if( hostResponsibleParty.value.responsible_party !== null ){
        if ( 'description' in hostResponsibleParty.value.responsible_party ){
          return hostResponsibleParty.value.responsible_party.description;
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
      if( hostResponsibleParty.value.role !== null ){
        if ( 'description' in hostResponsibleParty.value.role ){
          return hostResponsibleParty.value.role.description;
        }else{
          return "";
        }
      }else{
        return "Select role";
      }
    } );
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( hostResponsibleParty.value.host !== null ){
        if ( 'description' in hostResponsibleParty.value.host ){
          return hostResponsibleParty.value.host.description;
        }else{
          return "";
        }
      }else{
        return "Select host";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( hostResponsibleParty.value._user !== null ){
        if ( 'description' in hostResponsibleParty.value._user ){
          return hostResponsibleParty.value._user.description;
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
      if( hostResponsibleParty.value._status !== null ){
        if ( 'description' in hostResponsibleParty.value._status ){
          return hostResponsibleParty.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostResponsiblePartyRepo = useRepo(HostResponsibleParty);
    const hostResponsibleParty = ref(hostResponsiblePartyRepo.make());

    // function to create new object and to add to store
    const createHostResponsibleParty = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,hostResponsibleParty.value);
        await hostResponsiblePartyRepo.save(valueToSave);
        resetHostResponsibleParty();
    };

    const resetHostResponsibleParty = () => {
        Object.assign(hostResponsibleParty.value, hostResponsiblePartyRepo.make() );
    };

    return {
        hostResponsibleParty,
        createHostResponsibleParty,
        resetHostResponsibleParty,
        links,
        updateLinks,
        responsiblePartyOptions, responsiblePartyOptionsHint,
        roleOptions, roleOptionsHint,
        hostOptions, hostOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
