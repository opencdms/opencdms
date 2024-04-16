<template>
  <v-card>
    <v-card-title>Ingest data</v-card-title>
    <v-card-text>Ingest is currently supported via file upload to {{bucket}}</v-card-text>
  </v-card>
</template>

<script>
import { ref, defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';

export default defineComponent({
  name: 'data-ingest',
  props: {
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
  },
  methods: {},
  setup() {
    const bucket=ref("http://localhost:9000");
    bucket.value = process.env.BUCKET;
    console.log(bucket.value)
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
    return {bucket};
  }

});
</script>
