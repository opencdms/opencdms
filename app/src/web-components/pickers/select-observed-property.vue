// component to select station
<template>
  <v-autocomplete :items="options" item-title="id" item-value="id" label="observed property" v-model="selected" :hint="selected ? selected.standard_name : 'Select an observed property'" persistent-hint return-object/>
</template>
<script>
  // load host
  import ObservedProperty from '@/models/ObservedProperty'
  import {useRepo} from 'pinia-orm'
  import {computed, defineComponent, ref, watch} from 'vue';
  import {VAutocomplete} from 'vuetify/lib/components';
  export default defineComponent({
    name: "SelectObservedProperty",
    components: {
      VAutocomplete
    },
    emits: ["update:modelValue"],
    setup(props, {emit}) {
      const selected = ref(null);
      const options = computed( () => { return useRepo(ObservedProperty).all(); });
      console.log( options );
      const optionsHint = computed( () => {});
      watch( () => selected.value, (newValue) => {
        emit("update:modelValue", newValue)
      })
      return {selected, options};
    }
  });
</script>
