<template>
  <v-card>
    <v-card-title>Create new 'ReferenceSurface'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="referenceSurface.id"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="referenceSurface.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="referenceSurface.description"  hint="Description of reference surface" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createReferenceSurface">Create ReferenceSurface</v-btn>
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



// import model
import ReferenceSurface from '@/models/ReferenceSurface';

export default defineComponent({
  name: 'ReferenceSurfaceForm',
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
      referenceSurface.value.links = updatedLinks;
    }

    // set up repos

    const referenceSurfaceRepo = useRepo(ReferenceSurface);
    const referenceSurface = ref(referenceSurfaceRepo.make());

    // function to create new object and to add to store
    const createReferenceSurface = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,referenceSurface.value);
        await referenceSurfaceRepo.save(valueToSave);
        resetReferenceSurface();
    };

    const resetReferenceSurface = () => {
        Object.assign(referenceSurface.value, referenceSurfaceRepo.make() );
    };

    return {
        referenceSurface,
        createReferenceSurface,
        resetReferenceSurface,
        links,
        updateLinks
    }
  }
});
</script>
