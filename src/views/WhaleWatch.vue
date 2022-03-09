<template>
    <div class="whalewatching">
        <h1>Whale Watching</h1>
    </div>
    <br><br><br><br>
    <h2> What's hot?</h2>
    <grid :data="gridData" :columns="gridColumns"></grid>
    <br><br>
    <hr class="solid">
    <h1> Whale transactions of Bored Ape Yacht Club:</h1>
    <p> Hover for transaction destinations. <br>
        Red link = Sale <br>
        Blue link = Purchase </p>
    <div>
      <nodeChart/>
    </div>
    <br><br><br><br>
    <hr class="solid">
    <h2>Live Updating Whales</h2>
    <br><br><br><br>
</template>

<script>
import Grid from '../components/Grid'
import NodeChart from '../components/NodeChart.vue'
export default {
  name: "Whale watch",
    data() {
      return {
        gridData: [
          { collection: 'Bored Ape Yacht Club', last_7_days: 7, last_30_days: 45},
          { collection: 'Bored Ape Kennel Club', last_7_days: 98, last_30_days: 800},
          { collection: 'Cool Cats', last_7_days: 16, last_30_days: 67},
          { collection: 'Doodles', last_7_days: 44, last_30_days: 98},
          { collection: 'Crypto Punks', last_7_days: 21, last_30_days: 100},
          { collection: 'Clonex', last_7_days: 16, last_30_days: 101},
          { collection: 'Cryptoadz', last_7_days: 19, last_30_days: 165},
        ],
        gridColumns: ['collection', 'last_7_days', 'last_30_days'],        
      }
  },
  components: {
    Grid,
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
