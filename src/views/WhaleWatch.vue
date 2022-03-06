<template>
    <div class="whalewatching">
        <h1>Whale Watching</h1>
    </div>
    <br><br><br><br>
    <p> What's hot?</p>
    <grid :data="gridData" :columns="gridColumns"></grid>
    <br><br><br><br>
    <hr class="solid">
    <p>Insert Node Graph</p>
    <br><br><br><br>
    <hr class="solid">
    <p>Live Updating Whales</p>
    <br><br><br><br>
</template>

<script>
import Grid from '../components/Grid'
export default {
  name: "What's hot?",
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
    Grid
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
