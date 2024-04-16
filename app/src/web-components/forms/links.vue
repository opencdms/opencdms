<template>
  <v-card>
    <v-card-title>Add / edit links</v-card-title>
    <v-form>
      <v-card v-for="(link, index) in links" :key="index">
        <v-container>
          <v-row>
            <v-col cols="2"><v-text-field v-model="link.rel" label="rel" hint="IANA link relation, e.g. canonical, alternate" persistent-hint v-model.lazy="value"></v-text-field></v-col>
            <v-col cols="3"><v-text-field v-model="link.href" label="href" hint="URL for link" persistent-hint v-model.lazy="value"></v-text-field></v-col>
            <v-col cols="2"><v-text-field v-model="link.type" label="link type" hint="Result/link type, e.g. text/html" persistent-hint v-model.lazy="value"></v-text-field></v-col>
            <v-col cols="4"><v-text-field v-model="link.title" label="title" hint="Title / name of link" persistent-hint v-model.lazy="value"></v-text-field></v-col>
            <v-col cols="1"><v-btn color="error" @click="() => removeLink(index)"><v-icon>mdi-close</v-icon></v-btn></v-col>
          </v-row>
        </v-container>
      </v-card>
      <v-btn color="green" @click="addLink"><v-icon>mdi-plus</v-icon></v-btn>
    </v-form>
  </v-card>
</template>

<script>

import { defineComponent, ref, watch, context, computed, toRaw } from 'vue';
import { VForm, VTextField, VCard, VCardTitle, VBtn, VContainer, VRow, VCol, VIcon } from 'vuetify/lib/components';

export default defineComponent({
  name: 'LinkForm',
  components: {
    VForm,
    VTextField,
    VCard, VCardTitle,
    VBtn, VIcon,
    VContainer, VRow, VCol
  },
  props: {
    links: {
      type: Array,
      required: true
    },
  },
  emits: ["updateLinks"],
  setup(props, context) {
    const name = ref("");
    const description = ref("");
    //const location = ref("");
    const links = ref(props.links);

    watch( () => props.links, (value) => {
      if( typeof value === 'string'){
        links.value = JSON.parse(value);
      }else{
        links.value = value;
      }
    }, {immediate: true, deep: true} );

    // Update parent component when `links` changes
    watch( () => links.value, (value) => {
      context.emit('updateLinks', value);
    }, { deep: true });

    const addLink = () => {
      links.value.push({
        rel: "",
        href: "",
        type: "",
        title: ""
      });
    };
    const removeLink = (index) => {
      links.value = links.value.filter((link, i) => i !== index);
    };
    return {name, description, location, links, addLink, removeLink};
  }
});

</script>
