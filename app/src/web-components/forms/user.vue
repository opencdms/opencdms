<template>
  <v-card>
    <v-card-title>Create new 'User'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="user.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="user.name"  hint="Name of user/agent" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="user.description"  hint="Description of user / agent" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createUser">Create User</v-btn>
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
import User from '@/models/User';

export default defineComponent({
  name: 'UserForm',
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
      user.value.links = updatedLinks;
    }

    // set up repos

    const userRepo = useRepo(User);
    const user = ref(userRepo.make());

    // function to create new object and to add to store
    const createUser = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,user.value);
        await userRepo.save(valueToSave);
        resetUser();
    };

    const resetUser = () => {
        Object.assign(user.value, userRepo.make() );
    };

    return {
        user,
        createUser,
        resetUser,
        links,
        updateLinks
    }
  }
});
</script>
