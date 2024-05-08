<template>
  <div id="app">
    <strands/>
  </div>
</template>

<script>
import Strands from './components/Strands.vue'

export default {
  name: 'App',
  components: {
    Strands
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
