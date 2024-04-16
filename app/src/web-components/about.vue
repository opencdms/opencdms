<template>
  <v-card>
    <v-card-title>About</v-card-title>
    <v-card-text>Welcome to the OpenCDMS beta release demonstration site. This web application
    has been developed as part of the <a href="https://www.opencdms.org/">OpenCDMS project</a> and will form a reference
    implementation of the <a href="https://library.wmo.int/index.php?lvl=notice_display&id=16300">
    WMO Climate Data Management Systems specifications (WMO-No. 1131)</a>. The beta version is under development,
    with new features added weekly.  News articles and significant updates will be published at:
    <a href="https://openclimate.net/">https://openclimate.net/</a>. The web application has been built using open
    software and standards, the source code can be found in the project repository on GitHub:
    <a href="https://www.github.com/opencdms">https://www.github.com/opencdms</a>.
    </v-card-text>
  </v-card>
  <v-card>
    <v-card-title>Access control and authentication</v-card-title>
    <v-card-text>Access control and authentication has not been implemented in the
    current version of the software but will be implemented as part of the first release.
    The access control will be implemented at both the user and role level, with some users or roles
    only able to view data, other users able to edit a subset of the data and a small number with full
    access. Where the OpenCDMS interacts with other systems, for exampling publishing to the WMO Information
    System or updating records in OSCAR/Surface, the roles will be assigned to the respective national focal points.
    Only those users with appropriate roles will be able to edit and publish the relevant metadata.
    </v-card-text>
  </v-card>
  <v-card>
    <v-card-title>Acknowledgements - data</v-card-title>
    <v-card-item>
    <v-list :density="compact">
    <v-list-item style="font-size: 14px;">
      <v-list-item-title>Hourly climate observations</v-list-item-title>
      Example hourly climate observations have been downloaded from
      the <a href="https://api.weather.gc.ca/collections/climate-hourly">Environment and Climate
      Change Canada (ECCC) MSC GeoMet API</a>. This data has been accessed under the
      <a href="https://eccc-msc.github.io/open-data/licence/readme_en/">Environment and Climate Change
      Canada Data Servers End-use Licence</a>.
    </v-list-item>
    <v-list-item style=" font-size: 14px;">
      <v-list-item-title>Station metadata</v-list-item-title>
      Example station metadata have been downloaded from the
      <a href="https://api.weather.gc.ca/collections/climate-stations">Environment and Climate
      Change Canada (ECCC) MSC GeoMet API</a>. This data has been accessed under the
      <a href="https://eccc-msc.github.io/open-data/licence/readme_en/">Environment and Climate Change
      Canada Data Servers End-use Licence</a>.
    </v-list-item>
    <v-list-item style=" font-size: 14px;">
      <v-list-item-title>Watershed</v-list-item-title>
      Watershed boundaries come from the <a href="https://geohub.lio.gov.on.ca/maps/53a1c537b320404087c54ef09700a7db/explore?location=41.945997%2C-82.339420%2C4.94">
      Ontario Watershed Boundaries (OWB) collection</a>. These have been accessed under the <a href="https://www.ontario.ca/page/open-government-licence-ontario">Open Government Licence – Ontario</a> licence.
    </v-list-item>
    </v-list>
    </v-card-item>
  </v-card>
</template>

<script>
import { defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VList, VListItem, VListItemTitle } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
export default defineComponent({
  name: 'About',
  props: {
    title: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    }
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    VList,
    VListItem,
    VListItemTitle
  },
  methods: {},

});
</script>
