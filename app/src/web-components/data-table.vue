<template>
<v-container style="width: 100%;">
    <v-row>
      <v-col :cols="12">
        <v-card>
          <v-card-title>Select station</v-card-title>
          <v-card-text><select-host v-model="query_param.host"/></v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-if='query_param.host'>
      <v-col :cols="12">
        <v-card>
          <v-card-title>Select from available data for {{ $route.params.id }}</v-card-title>
          <v-card-item>
              <v-container>
                <v-row>
                  <v-col :cols="4"><select-observed-property v-model="query_param.observed_property"/></v-col>
                  <v-col :cols="4"><VueDatePicker text-input format="yyyy-MM-dd" :enable-time-picker="false" label="Start" v-model="query_param.start_date"  hint="Start date" persistent-hint :teleport="true"></VueDatePicker></v-col>
                  <v-col :cols="4"><VueDatePicker text-input format="yyyy-MM-dd" :enable-time-picker="false" label="End" v-model="query_param.end_date"  hint="End date" persistent-hint :teleport="true"></VueDatePicker></v-col>
                </v-row>
              </v-container>
            </v-card-item>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-if='query_param.host'>
      <v-col><v-card><v-btn @click="fetchData">Preview</v-btn></v-card></v-col>
      <v-col><v-card><v-btn @click="downloadData">Download</v-btn></v-card></v-col>
      <v-col><v-card><v-text-field hint="Number of records to download" persistent-hint label="Limit" v-model="maxItems" type="number" min="1"/></v-card></v-col>
    </v-row>
    <v-row>
      <v-col :cols="12">
      <v-card>
        <v-card-title>Results preview</v-card-title>
        <v-card-subtitle><a href="{{baseURL}}{{dataURL}}"></a>{{baseURL}}{{dataURL}}</v-card-subtitle>
        <v-card-text>
          <VDataTable :items="items" :headers="headers" dense small>
            <template v-slot:item.id="{ item }">
              <a :href="getIDLink(item.raw.id)">{{item.raw.id}}</a>
            </template>
            <template v-slot:item.links="{ item }">
              {{parseLinks(item.raw.links)}}
            </template>
          </VDataTable>
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
</v-container>

</template>

<script>
import { defineComponent, ref, watchEffect, computed, watch } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VTabs, VTab, VBtn, VAutocomplete, VCardSubtitle, VTextField } from 'vuetify/lib/components';
import { VDataTable } from 'vuetify/labs/VDataTable';
import { VContainer, VCol, VRow } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import { useRoute, useRouter } from 'vue-router';

import {useRepo} from 'pinia-orm';

import SelectHost from '@/web-components/pickers/select-host.vue';
import SelectObservedProperty from '@/web-components/pickers/select-observed-property.vue';

import VueDatePicker from '@vuepic/vue-datepicker';
//import VueDatePicker from '@/web-components/pickers/date-picker.vue';
import '@vuepic/vue-datepicker/dist/main.css';
import {formatISO, parseISO} from 'date-fns'
import * as d3 from 'd3';
import axios from 'axios';

import {TableLite} from 'vue3-table-lite';

// opencdms imports
import Host from '@/models/Host';
import {flatten_geojson} from '@/utils/geojson.js';
import {loadData} from '@/utils/load-data.js';

export default defineComponent({
  name: 'data-table',
  components: {
    VCard,
    VCardTitle, VCardSubtitle,
    VCardText,
    VCardItem,
    VTabs,
    VTab,
    VBtn, VTextField,
    VAutocomplete, VContainer, VCol, VRow,
    VDataTable,
    SelectHost,
    SelectObservedProperty,
    VueDatePicker,
    TableLite
  },
  methods: {
    parseLinks (links) {
      console.log(links)
      let res;
      if( links && links.length > 0 ){
        res = JSON.stringify(links);
      }else{
        res = '';
      }
      return res;
    },
    getIDLink (id) {
      return process.env.API + "/collections/observations/items/"+id;
    }
  },
  setup(props) {
    // set up varaiables
    const selectedHost = ref(null)
    const router = useRouter();
    const geom = ref(null);
    const dataURL = ref("");
    const start_date = ref(null);
    const end_date = ref(null);
    const baseURL = ref(process.env.API + "/collections/observations/items");
    const items = ref([]);
    const headers = ref([]);
    const maxItems = ref(null);
    const route = useRoute();
    const search = ref("");
    maxItems.value = 1000;

    const query_param = ref(
      {
        host:null,
        start_date: null,
        end_date: null,
        observed_property: null
      }
    );



    const fetchData =  async () => {
      console.log("Fetching" + process.env.API + "/collections/observations/items"+dataURL.value)
      items.value = [];
      var response = await loadData(process.env.API + "/collections/observations/items"+dataURL.value, true)
                          .then(result => flatten_geojson(result.features));
      items.value = response;
      console.log(items.value);
      headers.value = [
        {title: "Record ID", value: "id", key: "id", sortable: false},
        {title: "Date/time", value: "phenomenon_end", key: "phenomenon_end", sortable: false},
        {title: "Host", value: "host_id", key: "host_id", sortable: false},
        {title: "Observed property", value: "observed_property_id", key: "observed_property_id", sortable: false},
        {title: "Result value", value: "result_value", key: "result_value", sortable: false},
        {title: "Result units", value: "result_uom", key: "result_uom", sortable: false}
        //{title: "Result quality", value: "result_quality", key: "result_quality", sortable: false}
      ];
      console.log(items.value)
      console.log("Fetch complete")
    };


    onBeforeUnmount( () => {
        query_watch();
        items.value = null;
        selectedHost.value = null;
        geom.value = null;
        dataURL.value = null;
        start_date.value = null;
        end_date.value = null;
        baseURL.value = null;
        headers.value = null;
        maxItems.value = null;
    });
    onUnmounted( () => {
      console.log("Unmounted");
    });

    const downloadData = () => {
      var downloadURL = process.env.API + "/collections/observations/items"+dataURL.value.replace("f=json","f=csv").replace("limit=25", "limit="+maxItems.value);
      window.location.href = downloadURL;
    }

    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const host = ref(null)

    const query_watch = watch(query_param.value, () => {
      dataURL.value="?limit=25"
      if( query_param.value.host ){
        dataURL.value = dataURL.value + "&host_id=" + query_param.value.host.id
      }
      if( query_param.value.observed_property ){
        dataURL.value = dataURL.value + "&observed_property_id=" + query_param.value.observed_property.id
      }
      if( query_param.value.start_date && query_param.value.end_date){
        console.log(query_param.value.start_date.getDay());
        dataURL.value = dataURL.value + "&datetime="+formatISO(query_param.value.start_date).replace("+","%2B")+"/"+formatISO(query_param.value.end_date).replace("+","%2B")
      }
      dataURL.value = dataURL.value + "&f=json"
      console.log(query_param.value)
    }, {deep: true});



    onErrorCaptured( () => {});
    return {host, hostOptions, selectedHost, geom, start_date, end_date, downloadData, search,
            query_param, dataURL, formatISO, items, headers, baseURL, maxItems, fetchData};
  }

});

</script>
