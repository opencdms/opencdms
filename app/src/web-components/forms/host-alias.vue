<template>
  <v-card>
    <v-card-title>Create new 'HostAlias'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="hostAlias.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="hostAlias.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="alternative" v-model="hostAlias.alternative"  hint="Alternative ID by which the host is known" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="alternative_name" v-model="hostAlias.alternative_name"  hint="Alternative name by which the host is known" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="hostAlias.valid_from"  hint="Date the alternative id/name was used from" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="hostAlias.valid_to"  hint="Date the alternative id/name was used to" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="hostAlias._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="hostAlias._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="hostAlias._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="hostAlias._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="hostAlias.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHostAlias">Create HostAlias</v-btn>
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


import Host from '@/models/Host';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import HostAlias from '@/models/HostAlias';

export default defineComponent({
  name: 'HostAliasForm',
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
      hostAlias.value.links = updatedLinks;
    }

    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( hostAlias.value.host !== null ){
        if ( 'description' in hostAlias.value.host ){
          return hostAlias.value.host.description;
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
      if( hostAlias.value._user !== null ){
        if ( 'description' in hostAlias.value._user ){
          return hostAlias.value._user.description;
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
      if( hostAlias.value._status !== null ){
        if ( 'description' in hostAlias.value._status ){
          return hostAlias.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostAliasRepo = useRepo(HostAlias);
    const hostAlias = ref(hostAliasRepo.make());

    // function to create new object and to add to store
    const createHostAlias = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,hostAlias.value);
        await hostAliasRepo.save(valueToSave);
        resetHostAlias();
    };

    const resetHostAlias = () => {
        Object.assign(hostAlias.value, hostAliasRepo.make() );
    };

    return {
        hostAlias,
        createHostAlias,
        resetHostAlias,
        links,
        updateLinks,
        hostOptions, hostOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
