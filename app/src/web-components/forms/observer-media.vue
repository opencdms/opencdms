<template>
  <v-card>
    <v-card-title>Create new 'ObserverMedia'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observerMedia.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="observerOptions" item-title="name" item-value="id" label="observer" v-model="observerMedia.observer" :hint="observerOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="mediaOptions" item-title="name" item-value="id" label="media" v-model="observerMedia.media" :hint="mediaOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><VueDatePicker label="valid_from" v-model="observerMedia.valid_from"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><VueDatePicker label="valid_to" v-model="observerMedia.valid_to"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="observerMedia._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="_change_date" v-model="observerMedia._change_date"  hint="Date this record was changed" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observerMedia._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="observerMedia._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="observerMedia.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObserverMedia">Create ObserverMedia</v-btn>
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


import Observer from '@/models/Observer';
import Media from '@/models/Media';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import ObserverMedia from '@/models/ObserverMedia';

export default defineComponent({
  name: 'ObserverMediaForm',
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
      observerMedia.value.links = updatedLinks;
    }

    // set up repos
    const observerRepo = useRepo(Observer);
    const observerOptions = computed(() => { return observerRepo.all() });
    const observerOptionsHint = computed(() => {
      if( observerMedia.value.observer !== null ){
        if ( 'description' in observerMedia.value.observer ){
          return observerMedia.value.observer.description;
        }else{
          return "";
        }
      }else{
        return "Select observer";
      }
    } );
    const mediaRepo = useRepo(Media);
    const mediaOptions = computed(() => { return mediaRepo.all() });
    const mediaOptionsHint = computed(() => {
      if( observerMedia.value.media !== null ){
        if ( 'description' in observerMedia.value.media ){
          return observerMedia.value.media.description;
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
      if( observerMedia.value._user !== null ){
        if ( 'description' in observerMedia.value._user ){
          return observerMedia.value._user.description;
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
      if( observerMedia.value._status !== null ){
        if ( 'description' in observerMedia.value._status ){
          return observerMedia.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const observerMediaRepo = useRepo(ObserverMedia);
    const observerMedia = ref(observerMediaRepo.make());

    // function to create new object and to add to store
    const createObserverMedia = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observerMedia.value);
        await observerMediaRepo.save(valueToSave);
        resetObserverMedia();
    };

    const resetObserverMedia = () => {
        Object.assign(observerMedia.value, observerMediaRepo.make() );
    };

    return {
        observerMedia,
        createObserverMedia,
        resetObserverMedia,
        links,
        updateLinks,
        observerOptions, observerOptionsHint,
        mediaOptions, mediaOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
