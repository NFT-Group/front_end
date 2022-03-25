<template>
    <div class="whalewatching">
        <h1>Whale Watching</h1>
    </div>
    <br>
    <div>
      <nodeChart/>
    </div>
    <br><br><br><br>
    <hr class="solid">
    <h2>Live Updating Whales</h2>
    <br><br><br><br>
</template>

<script>
import NodeChart from '../components/NodeChart.vue'
export default {
  components: {
    NodeChart
  }
}
</script>

<style>
  p{
      font-weight: bold; 
  }
  hr.solid{
      border-top: 3px solid #bbb;
  }
  p.todo{
  font-style: italic;
  }
</style>
