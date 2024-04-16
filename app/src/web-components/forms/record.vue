<template>
  <v-card>
    <v-card-title>Create new 'Record'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="record.id"  hint="A unique identifier of the catalogue record." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="time" v-model="record.time"  hint="The temporal extent of the resource. Can be null if there is no associated temporal extent." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="title" v-model="record.title"  hint="A human-readable name given to the resource." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="location" v-model="record.location"  hint="A geometry associated with the resource that is used for discovery. Can be null if there is no associated geometry." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="created" v-model="record.created"  hint="Date of creation of this record." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="updated" v-model="record.updated"  hint="The most recent date on which the record was changed." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="resource_type" v-model="record.resource_type"  hint="The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="record.description"  hint="A free-text account of the resource." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="keywords" v-model="record.keywords"  hint="The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes. Semi-colon delimited" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="language" v-model="record.language"  hint="The natural language used for textual values (e.g. titles, descriptions, etc.) of the resource. ISO 639-1/639-2 codes should be used." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="external_ids" v-model="record.external_ids"  hint="An identifier for the resource assigned by an external (to the catalogue) entity." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="themes" v-model="record.themes"  hint="A knowledge organization system used to classify the resource." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="formats" v-model="record.formats"  hint="A list of available distributions of the resource." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="providers" v-model="record.providers"  hint="A list of providers qualified by their role in association to the record." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="license" v-model="record.license"  hint="A legal document under which the resource is made available. The value should be a code, convenient for filtering the records. Where applicable, the use of the identifiers from the SPDX License List is recommended. If multiple licenses apply, it is recommended to use ''various'.  Where available, links to a URI of each applicable license should be added to the 'links' property." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="rights" v-model="record.rights"  hint="A statement that concerns all rights not addressed by the license such as a copyright statement." persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
        </v-form>
        <v-btn @click="createRecord">Create Record</v-btn>
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
import Record from '@/models/Record';

export default defineComponent({
  name: 'RecordForm',
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
      record.value.links = updatedLinks;
    }

    // set up repos

    const recordRepo = useRepo(Record);
    const record = ref(recordRepo.make());

    // function to create new object and to add to store
    const createRecord = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,record.value);
        await recordRepo.save(valueToSave);
        resetRecord();
    };

    const resetRecord = () => {
        Object.assign(record.value, recordRepo.make() );
    };

    return {
        record,
        createRecord,
        resetRecord,
        links,
        updateLinks
    }
  }
});
</script>
