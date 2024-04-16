<template>
  <v-card>
    <v-card-title>Specification and roadmap</v-card-title>
    <v-card-text>The core functionality and requirements for a climate data management
    are defined in the <a href="https://library.wmo.int/index.php?lvl=notice_display&id=16300">
    WMO Climate Data Management Systems specifications (WMO-No. 1131)</a>. The specifications
    detailed in WMO-No. 1131 cover a range of topics, including policy and core IT infrastructure.
    Within the OpenCDMS project only the data management functions are considered, notably those covered
    by Section 4 to 8 of WMO-No. 1131. The cards below summarises these functions and progress
    towards their implementation. The full list of specifications can be found at
    <a href="https://spec.opencdms.org">https://spec.opencdms.org</a>.
    </v-card-text>
  </v-card>
  <v-expansion-panels v-if="requirements">
    <v-expansion-panel v-for="requirement in requirements" :title="requirement.title">
        <v-expansion-panel-text class="v-card-text">{{requirement.text}}
          <v-expansion-panels v-if="requirement.requirements" multiple>
            <v-expansion-panel v-for="r2 in requirement.requirements" :title="r2.title">
              <v-expansion-panel-text class="v-card-text">{{r2.text}}</v-expansion-panel-text>
              <v-expansion-panel-text>
              <v-card v-for="r3 in r2.requirements">
                <v-card-title>{{r3.title}} ({{r3.classification}})</v-card-title>
                <v-card-text>{{r3.text}}</v-card-text>
                <v-card :color="r3.color" :title="r3.status"/>
              </v-card>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import { ref, defineComponent } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/lib/components';
import { VExpansionPanels, VExpansionPanel, VExpansionPanelText } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'roadmap',
  props: {
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VExpansionPanel,
    VExpansionPanels,
    VExpansionPanelText
  },
  methods: {},
  setup() {

    const requirements=ref(null)

    const renderRequirement = (requirement) => {

    }

    // lifecycle hooks
    onBeforeMount( async () => {

    });
    onMounted( async() => {
      const response = await axios.get("/data/cdms-specs/specs.json")
      requirements.value = response.data
      console.log(requirements)
      // This hook is called after the component is mounted to the DOM.
      // This is a good place to perform any necessary DOM manipulations, initialize
      // third-party libraries, or set up event listeners.
    });
    return {requirements};
  }

});

</script>
