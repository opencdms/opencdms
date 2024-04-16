<template>
  <v-navigation-drawer>
    <OpenCDMSLogo/>
    <v-list :lines="false" density="compact" nav>
    <v-list-item router :to="{name: 'home'}" prepend-icon="mdi-home" title="Home"/>
    <v-list-group value="Stations">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-map-marker" title="Stations"></v-list-item>
      </template>
      <v-list-item router :to="{name: 'station-map'}" prepend-icon="mdi-map" title="Map view"/>
      <v-list-item router :to="{name: 'station-list'}" prepend-icon="mdi-table" title="Table view"/>
      <v-list-item router :to="{name: 'station-viewer'}" prepend-icon="mdi-pencil" title="View/edit"/>
      <v-list-item router :to="{name: 'host-form'}" prepend-icon="mdi-pencil" title="Create new"/>
      <v-list-item router :to="{name: 'station-import'}" prepend-icon="mdi-upload" title="Import"/>
    </v-list-group>
    <v-divider/>

    <v-list-group value="Sensors">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-thermometer" title="Sensors"/>
      </template>
      <v-list-item router :to="{name: 'sensor-list'}" prepend-icon="mdi-table" title="Table view"/>
      <v-list-item router :to="{name: 'sensor-viewer'}" prepend-icon="mdi-form-select" title="View single"/>
    </v-list-group>
    <v-divider/>


    <v-list-group value="Deployments">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-cog-clockwise" title="Deployments"/>
      </template>
      <v-list-item router :to="{name: 'deployment-list'}" prepend-icon="mdi-table" title="Table view"/>
      <v-list-item router :to="{name: 'deployment-viewer'}" prepend-icon="mdi-form-select" title="View single"/>
    </v-list-group>
    <v-divider/>

    <v-list-group value="Features">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-map-marker-circle" title="Features"/>
      </template>
      <v-list-item router :to="{name: 'feature-map'}" prepend-icon="mdi-map" title="Map"/>
      <v-list-item router :to="{name: 'feature-list'}" prepend-icon="mdi-table" title="Table"/>
      <v-list-item router :to="{name: 'feature'}" prepend-icon="mdi-form-select" title="View/edit"/>
    </v-list-group>
    <v-divider/>

    <v-list-group value="Data">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-table" title="Data"/>
      </template>
      <v-list-item router :to="{name: 'data-table'}" prepend-icon="mdi-table-search" title="Search"/>
      <!--<v-list-item router :to="{name: 'data-ingest'}" prepend-icon="mdi-database-arrow-left" title="data-ingest"/>-->
      <!--<v-list-item router :to="{name: 'data-extract'}" prepend-icon="mdi-database-arrow-right" title="data-extract"/>-->
      <!--<v-list-item router :to="{name: 'data-inventory'}" prepend-icon="mdi-abacus" title="data-inventory"/>-->
      <!--<v-list-item router :to="{name: 'data-map'}" prepend-icon="mdi-map" title="data-map"/>-->
      <v-list-item router :to="{name: 'data-station'}" prepend-icon="mdi-map-marker" title="data-station"/>
      <v-list-item router :to="{name: 'data-parameter'}" prepend-icon="mdi-thermometer" title="data-parameter"/>
    </v-list-group>
    <v-divider/>

    <!--
    <v-list-group value="Forms">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-spirit-level" title="Forms"/>
      </template>
      <v-list-item router :to="{name: 'observation-form'}" prepend-icon="mdi-spirit-level" title="observation-form"/>
      <v-list-item router :to="{name: 'observer-form'}" prepend-icon="mdi-spirit-level" title="New observer / sensor"/>
      <v-list-item router :to="{name: 'deployment-form'}" prepend-icon="mdi-spirit-level" title="New deployment"/>
      <v-list-item router :to="{name: 'source-form'}" prepend-icon="mdi-spirit-level" title="New source"/>
      <v-list-item router :to="{name: 'collection-form'}" prepend-icon="mdi-spirit-level" title="New collection"/>
    </v-list-group>
    <v-divider/>
    -->

    <!--
    <v-list-group value="Products">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-spirit-level" title="Products"/>
      </template>
      <v-list-item router :to="{name: 'product-climate-normal'}" prepend-icon="mdi-spirit-level" title="product-climate-normal"/>
      <v-list-item router :to="{name: 'product-climat'}" prepend-icon="mdi-spirit-level" title="product-climat"/>
      <v-list-item router :to="{name: 'product-daycli'}" prepend-icon="mdi-spirit-level" title="product-daycli"/>
    </v-list-group>
    <v-divider/>
    -->

    <!--
    <v-list-group value="Quality control">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-spirit-level" title="Quality control"/>
      </template>
      <v-list-item router :to="{name: 'quality-control'}" prepend-icon="mdi-spirit-level" title="quality-control"/>
    </v-list-group>
    <v-divider/>
    -->

    <!--
    <v-list-group value="Settings">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-spirit-level" title="Settings"/>
      </template>
      <v-list-item router :to="{name: 'settings-user'}" prepend-icon="mdi-spirit-level" title="settings-user"/>
    </v-list-group>
    <v-divider/>
    -->
    <v-list-group value="WIS2">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-web" title="WIS2"/>
      </template>
      <v-list-item router :to="{name: 'wis2-catalogue'}" prepend-icon="mdi-cloud-search" title="Catalogue"/>
    </v-list-group>
    <v-divider/>
    <v-list-item router :to="{name: 'roadmap'}" prepend-icon="mdi-map-marker-distance" title="Roadmap"/>
    <!--
    <v-list-group value="WIS2">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props" prepend-icon="mdi-web" title="WIS2"/>
      </template>
      <v-list-item router :to="{name: 'wis2-publication'}" prepend-icon="mdi-publish" title="Manage publications"/>
      <v-list-item router :to="{name: 'wis2-subscription'}" prepend-icon="mdi-spirit-level" title="Manage subscriptions"/>
      <v-list-item router :to="{name: 'wis2-catalogue'}" prepend-icon="mdi-cloud-search" title="Catalogue"/>
    </v-list-group>
    <v-divider/>
    -->

    </v-list>

  </v-navigation-drawer>
</template>

<script>
  import { VNavigationDrawer, VIcon, VListGroup, VList, VListItem, VListItemTitle, VImg, VDivider } from 'vuetify/lib/components'
  import { computed } from 'vue'
  // import { useStore } from 'vuex'
  import OpenCDMSLogo from './../web-components/opencdmsLogo'
  export default {
    name: 'AppSidebar',
    data () {
      return {
        drawer: true,
        rail: true,
      }
    },
    components: {
      VNavigationDrawer,
      VImg,
      VList,
      VListGroup,
      VListItem,
      VDivider,
      OpenCDMSLogo
    },
    setup() {
      //const store = useStore()
      return {  }
    },
  };

</script>
