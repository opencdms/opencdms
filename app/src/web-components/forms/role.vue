<template>
  <v-card>
    <v-card-title>Create new 'Role'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="role.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="authority" v-model="role.authority"  hint="Namelist authority" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="role.name"  hint="The name of the role" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="role.description"  hint="Description of the role" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createRole">Create Role</v-btn>
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
import Role from '@/models/Role';

export default defineComponent({
  name: 'RoleForm',
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
      role.value.links = updatedLinks;
    }

    // set up repos

    const roleRepo = useRepo(Role);
    const role = ref(roleRepo.make());

    // function to create new object and to add to store
    const createRole = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,role.value);
        await roleRepo.save(valueToSave);
        resetRole();
    };

    const resetRole = () => {
        Object.assign(role.value, roleRepo.make() );
    };

    return {
        role,
        createRole,
        resetRole,
        links,
        updateLinks
    }
  }
});
</script>
