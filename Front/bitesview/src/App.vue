<template>
  <div id="app">
    
    <Chart msg="Chart"/>
    


  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Chart from './components/Chart.vue'

export default {
  name: 'app',
  components: {
    Chart,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
