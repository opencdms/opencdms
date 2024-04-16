<template>
  <v-card>
    <v-card-title>Create new 'HostMedia'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="hostMedia.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="hostMedia.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="mediaOptions" item-title="name" item-value="id" label="media" v-model="hostMedia.media" :hint="mediaOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="hostMedia.valid_from"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="hostMedia.valid_to"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="hostMedia._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="hostMedia._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="hostMedia._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="hostMedia._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="hostMedia.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHostMedia">Create HostMedia</v-btn>
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
import Media from '@/models/Media';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import HostMedia from '@/models/HostMedia';

export default defineComponent({
  name: 'HostMediaForm',
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
      hostMedia.value.links = updatedLinks;
    }

    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( hostMedia.value.host !== null ){
        if ( 'description' in hostMedia.value.host ){
          return hostMedia.value.host.description;
        }else{
          return "";
        }
      }else{
        return "Select host";
      }
    } );
    const mediaRepo = useRepo(Media);
    const mediaOptions = computed(() => { return mediaRepo.all() });
    const mediaOptionsHint = computed(() => {
      if( hostMedia.value.media !== null ){
        if ( 'description' in hostMedia.value.media ){
          return hostMedia.value.media.description;
        }else{
          return "";
        }
      }else{
        return "Select media";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( hostMedia.value._user !== null ){
        if ( 'description' in hostMedia.value._user ){
          return hostMedia.value._user.description;
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
      if( hostMedia.value._status !== null ){
        if ( 'description' in hostMedia.value._status ){
          return hostMedia.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostMediaRepo = useRepo(HostMedia);
    const hostMedia = ref(hostMediaRepo.make());

    // function to create new object and to add to store
    const createHostMedia = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,hostMedia.value);
        await hostMediaRepo.save(valueToSave);
        resetHostMedia();
    };

    const resetHostMedia = () => {
        Object.assign(hostMedia.value, hostMediaRepo.make() );
    };

    return {
        hostMedia,
        createHostMedia,
        resetHostMedia,
        links,
        updateLinks,
        hostOptions, hostOptionsHint,
        mediaOptions, mediaOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
