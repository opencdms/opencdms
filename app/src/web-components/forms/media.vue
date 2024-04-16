<template>
  <v-card>
    <v-card-title>Create new 'Media'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="media.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="mediaTypeOptions" item-title="name" item-value="id" label="media_type" v-model="media.media_type" :hint="mediaTypeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="description" v-model="media.description"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><VueDatePicker label="created" v-model="media.created"  hint="" persistent-hint></VueDatePicker></v-card-item>
            <v-card-item><v-text-field label="creator" v-model="media.creator"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="rights" v-model="media.rights" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="source" v-model="media.source"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="data" v-model="media.data"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createMedia">Create Media</v-btn>
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


import MediaType from '@/models/MediaType';

// import model
import Media from '@/models/Media';

export default defineComponent({
  name: 'MediaForm',
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
      media.value.links = updatedLinks;
    }

    // set up repos
    const mediaTypeRepo = useRepo(MediaType);
    const mediaTypeOptions = computed(() => { return mediaTypeRepo.all() });
    const mediaTypeOptionsHint = computed(() => {
      if( media.value.media_type !== null ){
        if ( 'description' in media.value.media_type ){
          return media.value.media_type.description;
        }else{
          return "";
        }
      }else{
        return "Select media_type";
      }
    } );

    const mediaRepo = useRepo(Media);
    const media = ref(mediaRepo.make());

    // function to create new object and to add to store
    const createMedia = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,media.value);
        await mediaRepo.save(valueToSave);
        resetMedia();
    };

    const resetMedia = () => {
        Object.assign(media.value, mediaRepo.make() );
    };

    return {
        media,
        createMedia,
        resetMedia,
        links,
        updateLinks,
        mediaTypeOptions, mediaTypeOptionsHint
    }
  }
});
</script>
