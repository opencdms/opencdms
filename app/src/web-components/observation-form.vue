<template>
  <v-card>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-text>{{ content }}</v-card-text>
    <v-card-text>{{ description }}</v-card-text>
  </v-card>
  <v-card v-if='obsLoaded'>
    <v-card-title>Example line plot</v-card-title>
    <v-card-item><Line :data="chartData"/></v-card-item>
  </v-card>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import {loadData} from '@/utils/load-data.js';

import {Line} from 'vue-chartjs';
import { Chart, CategoryScale, LinearScale, LineController, LineElement, PointElement} from 'chart.js';
Chart.register(CategoryScale, LinearScale, LineController, LineElement, PointElement);

export default defineComponent({
  name: 'observation-form',
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
    Line
  },
  methods: {},
  setup() {
    const obs = ref(null);
    const obsLoaded = ref(false);
    const chartOptions = ref({
      scales: {
        x: {
          type: "time"
        }
      }
    });

    onMounted(async () => {
      obs.value = await loadData('/data/example_obs.csv');
      obsLoaded.value = true;
    });

    const chartData = computed(() => {
      if (obs.value) {
        console.log(obs.value);
        let retval = {
          // labels: obs.value.map(d => new Date(d.date)),
          labels: obs.value.map(d => d.date),
          datasets: [
            {
              label: 'Air temperature',
              data: obs.value.map(d => d.air_temperature)
            }
          ]
        };
        console.log(retval);
        return retval;
      } else {
        return {};
      }
    });
    return {obs, chartData, obsLoaded};
  }

});
</script>
