<template>
  <v-container>
    <v-card>
      <v-card-title>Import station from OSCAR/Surface</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field clearable :rules="[rules.validWSI]" label="WIGOS Identifier" v-model="wigos_identifier"/>
          <v-btn @click="search">Search</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  import { defineComponent, ref, watchEffect, computed, watch } from 'vue';
  import { VCard, VCardTitle, VCardText, VCardItem, VTabs, VTab, VBtn, VAutocomplete, VCardSubtitle, VTextField } from 'vuetify/lib/components';
  import { VContainer, VForm } from 'vuetify/lib/components';

  // opencdms imports
  import Host from '@/models/Host';
  import {flatten_geojson} from '@/utils/geojson.js';
  import {loadData} from '@/utils/load-data.js';
  import { useRoute, useRouter } from 'vue-router';
  import {useRepo} from 'pinia-orm';


  export default defineComponent({
    name: 'import-wmdr-host',
    components: {
      VContainer, VBtn, VForm, VTextField,
      VCard, VCardTitle, VCardText
    },
    setup(props, {context}){
      const router = useRouter();
      const wigos_identifier = ref("");
      const rules = ref({
        validWSI: value => /^0-[0-9]{1,5}-[0-9]{0,5}-[0-9a-zA-Z]{1,16}$/.test(value) || 'Invalid WSI',
      });

      const search = async () => {
        //var oscar_url = "https://oscar.wmo.int/surface/rest/api/search/station?wigosId=";
        //var query = oscar_url + wigos_identifier.value;
        //console.log(query);
        //var stations = await fetch(query).then(response => response.json());
        //console.log(stations);
        var payload = {
          "inputs": {
            WIGOS_identifier: wigos_identifier.value
          },
          "outputs": {
            "status": null
          }
        }
        payload = JSON.stringify(payload);
        var url_ = process.env.API + "/processes/ingestHost/execution"
        var response = await fetch( url_, {
          method: 'POST',
          body: payload,
          headers: {
            encode: 'json'
          }
        });

        if(response.ok){
          // load new host and navigate to details
          var station_id = wigos_identifier.value
          var new_host = await loadData(process.env.API + '/collections/stations/items/'+station_id + "?f=json", true)
                              .then( (result) => flatten_geojson(result.features ? result.features : [result]) )
                              .then( (result) => { useRepo(Host).save(result) });
          router.push('/station/'+wigos_identifier.value);
        }else{
          console.log(response);
        }
      };
      return {rules, search, wigos_identifier};
    }
  });


</script>
