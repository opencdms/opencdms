<template>
  <div>
    <feature-map geom="Hello"/>
  </div>
</template>

<script>
import FeatureMap from '@/web-components/maps/feature-map';

export default {
  name: 'MyView',
  components: {
    FeatureMap,
  },
};
</script>

<style>
</style>
