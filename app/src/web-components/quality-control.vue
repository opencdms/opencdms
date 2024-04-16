<template>
  <v-card>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-text>{{ content }}</v-card-text>
    <v-card-text>{{ description }}</v-card-text>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
export default defineComponent({
  name: 'quality-control',
  props: {
    title: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
  },
  methods: {},
  setup() {
    // lifecycle hooks
    onBeforeMount( () => {
      // This hook is called before the component is mounted to the DOM.
      // This is a good place to do any necessary setup before the component is visible.
    });
    onMounted( () => {
      // This hook is called after the component is mounted to the DOM.
      // This is a good place to perform any necessary DOM manipulations, initialize
      // third-party libraries, or set up event listeners.
    });
    onBeforeUpdate( () => {
      // This hook is called when a component's data changes, but before the DOM is re-rendered.
      // This is a good place to make any necessary calculations or changes before the component
      // is updated.
    });
    onUpdated( () => {
      // This hook is called after the component is updated and the DOM is re-rendered.
      // This is a good place to perform any necessary DOM manipulations or update third-party
      // libraries.
    });
    onBeforeUnmount( () => {
      // This hook is called before the component is unmounted from the DOM.
      // This is a good place to clean up any resources or event listeners that were set up in
      // onMounted.
    });
    onUnmounted( () => {
      // This hook is called after the component is unmounted from the DOM.
      // This is a good place to perform any final cleanup or tear down of resources.
    });
    onErrorCaptured( () => {});
  }

});
</script>
