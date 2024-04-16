<template>
  <v-container>
    <v-row>
      <select-host/>
      <select-observed-property/>
      <VueDatePicker range/>
    </v-row>
    <v-row>
      <v-card v-if='obsLoaded'>
        <v-card-title>Example line plot</v-card-title>
        <v-card-item><Line :data="chartData"/></v-card-item>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
  import SelectHost from '@/web-components/pickers/select-host.vue';
  import SelectObservedProperty from '@/web-components/pickers/select-observed-property.vue';
  import SelectDate from '@/web-components/pickers/date-picker.vue';

  import {VContainer, VRow} from 'vuetify/lib/components';

  import {ref} from 'vue';

  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'


  export default {
    name: '',
    components: {
      SelectHost,
      SelectObservedProperty,
      SelectDate, VueDatePicker,
      VContainer, VRow
    },
    setup() {
    const date = ref();
    return {
      date
    }
  }
  };
</script>
