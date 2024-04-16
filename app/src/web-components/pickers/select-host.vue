// component to select station
<template>
  <v-autocomplete :items="options" item-title="name" item-value="id" label="host" v-model="selected" :hint="selected ? selected.name : 'Select a host'" persistent-hint return-object/>
</template>
<script>
  // load host
  import Host from '@/models/Host'
  import {useRepo} from 'pinia-orm'
  import {computed, defineComponent, ref, watch} from 'vue';
  import {VAutocomplete} from 'vuetify/lib/components';
  export default defineComponent({
    name: "SelectHost",
    components: {
      VAutocomplete
    },
    emits: ["update:modelValue"],
    setup(props, {emit}) {
      const selected = ref(null);
      const options = computed( () => { return useRepo(Host).all(); });
      console.log( options );
      const optionsHint = computed( () => {});
      watch( () => selected.value, (newValue) => {
        emit("update:modelValue", newValue)
      })
      return {selected, options};
    }
  });
</script>
