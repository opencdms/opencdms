<template>
  <v-card>
    <v-card-title>Sensors</v-card-title>
    <v-card-text>
      <VTextField style="width: 400px;" v-model="search" prepend-icon="mdi-text-search" label="search" single-line hide-details></VTextField>
      <VDataTable :headers="headers" :items="items" :search="search" dense small>
          <template v-slot:item.id="{ item }">
            <a :href="getIDLink(item.raw.id)">{{item.raw.id}}</a>
          </template>
          <template v-slot:item.links="{ item }">
            {{parseLinks(item.raw.links)}}
          </template>
      </VDataTable>
    </v-card-text>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText, VChip } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import { ref, computed, watchEffect, watch } from 'vue'
import { VDataTable } from 'vuetify/labs/VDataTable';
import { VTextField } from 'vuetify/lib/components';
import {useRepo} from 'pinia-orm';
import * as d3 from 'd3';

// opencdms components

import Observer from '@/models/Observer';

export default defineComponent({
  name: 'station-list',
  props: {
    connection: {
      type: String,
      default: "/data/observers.psv"
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VDataTable,
    VTextField,
  },
  methods: {
    parseLinks (links) {
      let res;
      if( links && links.length > 0 ){
        res = JSON.stringify(links);
      }else{
        res = '';
      }
      return res;
    },
    getIDLink (id) {
      return '/#/sensor/'+id;
    }
  },
  setup(props) {
    const headers = ref([]);
    const data = ref([]);
    const search = ref("");
    const sortBy = ref([{key:"", order:"desc"}]);
    const items = ref([]);
    const selected = ref([]);

    const observerRepo = useRepo(Observer);

    console.log(useRepo(Observer).piniaStore());

    const loadCSV = async (path) => {
      let csvData;
      csvData = await d3.dsv('|',path, d3.autoType);
      return {csvData};
    };

    onMounted( async() => {
        items.value = observerRepo.all();
        headers.value = Object.keys(items.value[0]).map( key => ({
          title: key,
          value: key,
          key: key,
          sortable: true
        }));
        console.log(observerRepo.all()) ;

      console.log(headers);
      console.log(observerRepo.all());
    });
    return {headers, items, search, sortBy};
  }

});
</script>
