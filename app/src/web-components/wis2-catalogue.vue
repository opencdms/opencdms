<template>
  <v-card>
    <v-card-title>
      WIS2.0 Catalogue Search
    </v-card-title>
    <v-container>
      <v-row>
        <v-col :cols="6">
          <v-form>
            <v-text-field label="min-x" v-model="minx"/>
            <v-text-field label="min-y" v-model="miny"/>
            <v-text-field label="max-x" v-model="maxx"/>
            <v-text-field label="max-y" v-model="maxy"/>
            <v-textarea label="Keywords (semi-colon (;) delimited)" v-model="keywords"/>
            <v-btn @click="searchCatalogue">Search</v-btn>
          </v-form>
        </v-col>
        <v-col :cols="6">
          <v-card style="height: 600pt;">
            <v-card-text style="height: 100%;"><base-map @mapLoaded='onMapLoaded' id="map" @click="mapEvent" zoom="3"/></v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  <v-card>
    <v-card-title>
      {{collections.features.length}} results
    </v-card-title>
    <v-card v-for="collection in collections.features">
      <v-card-title>{{collection.properties.title}}</v-card-title>
      <v-card-subtitle>{{collection.id}}</v-card-subtitle>
      <v-card-text>
        <v-container>
          <v-row style="min-height: 100px;">
            <v-col :cols="12">
              {{collection.properties.description}}
            </v-col>
          </v-row>
      </v-container>
      </v-card-text>
      <v-card-actions>
        <v-btn size="small" @click="moreInformation(collection)">More information</v-btn>
        <v-btn size="small" @click="parseLinks(collection)">Subscribe</v-btn>
      </v-card-actions>
    </v-card>
  </v-card>
</template>

<script>
import { defineComponent, ref, watch } from 'vue';
import { VCard, VCardTitle, VCardText, VForm, VTextField, VTextarea, VContainer, VRow, VCol, VBtn, VCardSubtitle, VCardActions } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import { VFor } from 'vuetify/lib/directives';

import {useRepo} from 'pinia-orm';

import BaseMap from "@/web-components/maps/base-map.vue";
import FeatureMap from "@/web-components/maps/feature-map.vue";

import MQTTSubscription from '@/models/MQTTSubscription.js';

export default defineComponent({
  name: 'wis2-subscription',
  props: {
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VForm, VTextField, VTextarea, VBtn,
    VContainer, VRow, VCol, VFor,
    BaseMap, FeatureMap, VCardSubtitle, VCardActions
  },
  methods: {},
  setup(props, {emit}) {
    const map = ref(null);

    const minx = ref(-180);
    const miny = ref(-90);
    const maxx = ref(180);
    const maxy = ref(90);
    const keywords = ref(null);
    const collections = ref({features: []});

    const MQTTSubRepo = ref(null);
    const useMQTTSub = ref(null);

    MQTTSubRepo.value = useRepo(MQTTSubscription);

    const onMapLoaded = async (mapInstance) => {
        map.value = mapInstance;
    };

    const mapEvent = (e) =>{
      var bounds = map.value.getBounds();
      minx.value = bounds.getWest();
      miny.value = bounds.getSouth();
      maxx.value = bounds.getEast();
      maxy.value = bounds.getNorth();
    };

    const searchCatalogue = async () => {
      var bbox = `&bbox=${minx.value},${miny.value},${maxx.value},${maxy.value}`;
      var query = "?";//q=mqtt";
      if( ! (keywords.value == null) ){
        if( keywords.value.endsWith(";") ){
          keywords.value = keywords.value.slice(0, -1);
        }
        query = query + "q=" + keywords.value.replace(/;/g," AND ");
      }else{
        console.log(! (keywords.value == null) )
        console.log(keywords.value)
      }
      console.log(query+bbox);
      const baseurl = "https://api.weather.gc.ca/collections/wis2-discovery-metadata/items"
      const url = `${baseurl}${query}${bbox}`;
      console.log( url );
      const response = await fetch(url);
      const data = await response.json();
      console.log(data);
      collections.value = data;
    }

    const parseLinks = (collection) => {
      for( const link of collection.links ){
        if( link.rel == "data" && (link.type == "MQTT" || link.type == "mqtt")){  // use toLower or similar. Not working, and neither is my brain.
          console.log("MQTT found");
          console.log( link );
          var sub = {
            id: collection.id,
            topic: link['wmo:topic'] ? link['wmo:topic'] : link['channel'],
            bucket: "wis2subs",
            process: "ingestBUFR",
            subscribed: true
          }
          useRepo(MQTTSubscription).insert(sub);
          console.log(useRepo(MQTTSubscription).all());
        }else{
          console.log("No MQTT");
        }
      }
    }


    const moreInformation = (collection) => {
      var url_ = "https://api.weather.gc.ca/collections/wis2-discovery-metadata/items/"+collection.id;
      window.open(url_);
    }


    return {mapEvent, onMapLoaded, minx, miny, maxx, maxy, keywords, parseLinks,
            searchCatalogue, collections, moreInformation};

  }

});
</script>
