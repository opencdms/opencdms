<template>
  <v-card>
    <v-card-title>{{ route.params.id ? 'Edit' : 'Create new' }} station details</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="host.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="host.name"  hint="Preferred name of host" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="host.description"  hint="Description of host" persistent-hint></v-text-field></v-card-item>
            <v-card-item><geometry-picker v-model="host.location" style="height: 100%"/></v-card-item>
            <v-card-item><v-text-field label="elevation" v-model="host.elevation" type="number" hint="Elevation of station above mean sea level in meters" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="wigos_station_identifier" v-model="host.wigos_station_identifier"  hint="WIGOS station identifier" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-autocomplete :items="facilityTypeOptions" item-title="name" item-value="id" label="facility_type" v-model="host.facility_type" :hint="facilityTypeOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item>
              <v-container>
                <v-row>
                  <v-col :cols="4"><VueDatePicker label="date_established" v-model="host.date_established"  hint="Date host was first established" persistent-hint></VueDatePicker></v-col>
                  <v-col :cols="4"><VueDatePicker label="date_closed" v-model="host.date_closed"  hint="Date host was first established" persistent-hint></VueDatePicker></v-col>
                </v-row>
              </v-container>
            </v-card-item>
            <v-card-item><v-autocomplete :items="wmoRegionOptions" item-title="name" item-value="id" label="wmo_region" v-model="host.wmo_region" :hint="wmoRegionOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item><v-autocomplete :items="territoryOptions" item-title="name" item-value="id" label="territory" v-model="host.territory" :hint="territoryOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item><v-autocomplete :items="timeZoneOptions" item-title="name" item-value="id" label="time_zone" v-model="host.time_zone" :hint="timeZoneOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item>
              <v-container>
                <v-row>
                  <v-col :cols="4"><VueDatePicker label="valid_from" v-model="host.valid_from"  hint="Date from which the details for this record are valid" persistent-hint></VueDatePicker></v-col>
                  <v-col :cols="4"><VueDatePicker label="valid_to" v-model="host.valid_to"  hint="Date after which the details for this record are no longer valid" persistent-hint></VueDatePicker></v-col>
                </v-row>
              </v-container>
            </v-card-item>
            <v-card-item><LinkForm :links="host.links" @updateLinks="(value) => host.links = value" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="host._version" type="number" hint="Version number of this record (autoupdated)" persistent-hint readonly></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_change_date" v-model="host._change_date"  hint="Date this record was changed (autoupdated)" persistent-hint readonly></v-text-field></v-card-item>
            <v-card-item><v-autocomplete :items="userOptions" item-title="name" item-value="id" label="user" v-model="host._user" :hint="userOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item><v-autocomplete :items="statusOptions" item-title="name" item-value="id" label="status" v-model="host._status" :hint="statusOptionsHint" return-object persistent-hint></v-autocomplete></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="host.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHost">{{ route.params.id ? 'Save' : 'Create' }}</v-btn>
        <v-btn @click="cancelEdit">Cancel</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
import * as d3 from 'd3';
import { defineComponent, ref, computed, watch } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VForm, VTextField, VSelect, VBtn, VAutocomplete } from 'vuetify/lib/components';
import { VContainer, VRow, VCol } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import {useStore} from 'pinia';
import {useRepo} from 'pinia-orm';

import LinkForm from '@/web-components/forms/links';
import VueDatePicker from '@/web-components/pickers/date-picker.vue';
import GeometryPicker from '@/web-components/pickers/geometry.vue';

import {useRoute, useRouter} from 'vue-router';


import FacilityType from '@/models/FacilityType';
import WmoRegion from '@/models/WmoRegion';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Host from '@/models/Host';

export default defineComponent({
  name: 'HostForm',
  props: {
  },
  methods:{
    parseLinks (links) {
      let res;
      if( links && links.length > 0 ){
        res = JSON.stringify(links);
      }else{
        res = '';
      }
      return res;
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    VTextField,
    VSelect, VAutocomplete,
    VForm,
    VBtn,
    VueDatePicker,
    GeometryPicker,
    LinkForm,
    VContainer, VCol, VRow
  },
  setup() {

    const route = useRoute();
    const router = useRouter();

    // set up links object
    const links = ref([]);
    const updateLinks = (updatedLinks) => {
      console.log("updating links");
      host.value.links = updatedLinks;
    }

    // set up repos
    const facilityTypeRepo = useRepo(FacilityType);
    const facilityTypeOptions = computed(() => { return facilityTypeRepo.all() });
    const facilityTypeOptionsHint = computed(() => {
      if( host.value.facility_type ){
        if ( 'description' in host.value.facility_type ){
          return host.value.facility_type.description;
        }else{
          return "";
        }
      }else{
        return "Select facility_type";
      }
    } );
    const wmoRegionRepo = useRepo(WmoRegion);
    const wmoRegionOptions = computed(() => { return wmoRegionRepo.all() });
    const wmoRegionOptionsHint = computed(() => {
      if( host.value.wmo_region ){
        if ( 'description' in host.value.wmo_region ){
          return host.value.wmo_region.description;
        }else{
          return "";
        }
      }else{
        return "Select wmo_region";
      }
    } );
    const territoryRepo = useRepo(Territory);
    const territoryOptions = computed(() => { return territoryRepo.all() });
    const territoryOptionsHint = computed(() => {
      if( host.value.territory ){
        if ( 'description' in host.value.territory ){
          return host.value.territory.description;
        }else{
          return "";
        }
      }else{
        return "Select territory";
      }
    } );
    const timeZoneRepo = useRepo(TimeZone);
    const timeZoneOptions = computed(() => { return timeZoneRepo.all() });
    const timeZoneOptionsHint = computed(() => {
      if( host.value.time_zone ){
        if ( 'description' in host.value.time_zone ){
          return host.value.time_zone.description;
        }else{
          return "";
        }
      }else{
        return "Select time_zone";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( host.value._user ){
        if ( 'description' in host.value._user ){
          return host.value._user.description;
        }else{
          return "";
        }
      }else{
        return "Select user";
      }
    } );
    const statusRepo = useRepo(Status);
    const statusOptions = computed(() => { return statusRepo.all() });
    const statusOptionsHint = computed(() => {
      if( host.value._status ){
        if ( 'description' in host.value._status ){
          return host.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostRepo = useRepo(Host);
    const host = ref(null);

    console.log(route.params);
    if( route.params.id ){
      // get host with eager loading
      host.value = useRepo(Host).
          with('territory').
          with('wmo_region').
          with('facility_type').
          with('time_zone').
          with('_user').
          with('_status').
          where('id',route.params.id).first();
      console.log( host.value );
    }else{
      host.value = useRepo(Host).make()
    }

    // const host = ref(hostRepo.make());

    // function to create new object and to add to store
    const createHost = async () => {
        console.log("saving");
        console.log(host.value)
        let valueToSave = {};
        Object.assign(valueToSave,host.value);
        await hostRepo.save(valueToSave);
        // navigate to view new record
        router.push('/station/'+ host.value.id);
    };
    const cancelEdit = async () => {
        router.push('/station/'+route.params.id);
    };

    watch( (host.value), (data)  => {
      console.log(data)
    })

    const resetHost = () => {
        Object.assign(host.value, hostRepo.make() );
    };

    onMounted( () => {
      // This hook is called after the component is mounted to the DOM.
      // This is a good place to perform any necessary DOM manipulations, initialize
      // third-party libraries, or set up event listeners.
      if( route.params.id ){
        host.value._version = host.value._version + 1;
      }else{
        host.value._version = 1;
        host.value._user = useRepo(User).where('id','tag:beta.opencdms.org,2023:/data/user/default').first();
        host.value._status = useRepo(Status).where('id','tag:beta.opencdms.org,2023:/vocab/status/draft').first();
      }
    });

    return {
        host,
        createHost, cancelEdit,
        resetHost,
        links,
        updateLinks,
        facilityTypeOptions, facilityTypeOptionsHint,
        wmoRegionOptions, wmoRegionOptionsHint,
        territoryOptions, territoryOptionsHint,
        timeZoneOptions, timeZoneOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint,
        route
    }
  }
});
</script>
