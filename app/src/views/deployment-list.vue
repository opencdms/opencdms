<template>
  <div>
    <deployment-list title="deployment-list" content="This page is under construction" description="list of deployed sensors" />
  </div>
</template>

<script>
import DeploymentList from './../web-components/deployment-list.vue';


export default {
  name: 'MyView',
  components: {
    DeploymentList,
  },
};
</script>

<style>
</style>
