<template>
  <v-card>
    <v-card-title>{{label}}</v-card-title>
    <v-card-item><VueDatePicker v-model="selectedDate" :format="format" inline text-input inline-with-input></VueDatePicker></v-card-item>
  </v-card>
</template>

<script>
import { defineComponent, ref, watch, context } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker';
import { VCard, VCardTitle, VCardText, VCardItem, VForm, VTextField, VSelect, VBtn } from 'vuetify/lib/components';
import '@vuepic/vue-datepicker/dist/main.css';
import {formatISO, parseISO} from 'date-fns'
export default defineComponent({
  name: 'date-picker',
  components: {
    VueDatePicker, formatISO, VCard, VCardTitle, VCardItem
  },
  props: {
    label: {
      type: String,
      default: 'Pick a date'
    },
    modelValue: {
      type: String,
      required: true
    },
  },
  emits: ["update:modelValue"],
  setup(props, {emit} ) {
    const selectedDate = ref(props.modelValue || '');
    const format = (date) => {
      return formatISO(date);
    };
    watch( () => props.modelValue,
      (newValue) => {
        selectedDate.value = parseISO(newValue);
      },
      {immediate: true}
     );

    watch(selectedDate, (newValue) => {
      if( format(newValue) !== props.modelValue){
        emit('update:modelValue', format(newValue));
      }
    });

    return {
      selectedDate, format
    };
  }
});
</script>
