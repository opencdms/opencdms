<template>
  <v-card>
    <v-card-title>Create new 'ResponsibleParty'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="responsibleParty.id"  hint="A value uniquely identifying a party (individual or organization)." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="responsibleParty.name"  hint="The name of the organization or the individual." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="position_name" v-model="responsibleParty.position_name"  hint="Role or position of the responsible person." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="organization" v-model="responsibleParty.organization"  hint="Organization/affiliation of the individual/responsible person. In case of an organization, the name property should be used and this property is not to be used." persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="logo" v-model="responsibleParty.logo"  hint="Graphic identifying a party" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="contact_information" v-model="responsibleParty.contact_information"  hint="Contact information" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createResponsibleParty">Create ResponsibleParty</v-btn>
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
import ResponsibleParty from '@/models/ResponsibleParty';

export default defineComponent({
  name: 'ResponsiblePartyForm',
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
      responsibleParty.value.links = updatedLinks;
    }

    // set up repos

    const responsiblePartyRepo = useRepo(ResponsibleParty);
    const responsibleParty = ref(responsiblePartyRepo.make());

    // function to create new object and to add to store
    const createResponsibleParty = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,responsibleParty.value);
        await responsiblePartyRepo.save(valueToSave);
        resetResponsibleParty();
    };

    const resetResponsibleParty = () => {
        Object.assign(responsibleParty.value, responsiblePartyRepo.make() );
    };

    return {
        responsibleParty,
        createResponsibleParty,
        resetResponsibleParty,
        links,
        updateLinks
    }
  }
});
</script>
