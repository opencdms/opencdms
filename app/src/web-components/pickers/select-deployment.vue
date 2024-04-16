// component to select station
<template>
  <v-autocomplete :items="options" item-title="id" item-value="id" label="deployment" v-model="selected" :hint="selected ? selected.name : 'Select an deployment'" persistent-hint return-object/>
</template>
<script>
  // load deployment
  import Deployment from '@/models/Deployment'
  import {useRepo} from 'pinia-orm'
  import {computed, defineComponent, ref, watch} from 'vue';
  import {VAutocomplete} from 'vuetify/lib/components';
  export default defineComponent({
    name: "SelectDeployment",
    components: {
      VAutocomplete
    },
    emits: ["update:modelValue"],
    setup(props, {emit}) {
      const selected = ref(null);
      const options = computed( () => { return useRepo(Deployment).all(); });
      console.log( options );
      const optionsHint = computed( () => {});
      watch( () => selected.value, (newValue) => {
        emit("update:modelValue", newValue)
      })
      return {selected, options};
    }
  });
</script>
