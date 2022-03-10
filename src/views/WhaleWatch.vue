<template>
    <div class="whalewatching">
        <h1>Whale Watching</h1>
    </div>
    <br>
    <h2> What's hot?</h2>
    <grid :data="gridData" :columns="gridColumns"></grid>
    <br><br>
    <hr class="solid">
    <h1> Whale transactions node graph:</h1>
    <form @submit="onSubmit">
      <label>Choose a Collection:</label>
        <select value="collection" id="collection" name="collection">
            <option value="punk" id="punk" name="collection">CryptoPunks</option>
            <option value="boredape" id="boredape" name="collection">Bored Ape Yacht Club</option>
            <option value="boredapekennel" id="boredapekennel" name="collection">Bored Ape Kennel Club</option>
            <option value="doodle" id="doodle" name="collection">Doodles</option>
            <option value="coolcat" id="coolcat" name="collection">Cool Cats</option>
            <option value="cryptoad" id="cryptoad" name="collection">CrypToadz</option>
            <option value="penguin" id="penguin" name="collection">Pudgy Penguins</option>
            <option value="clonex" id="clonex" name="collection">cloneX</option>
        </select>
    </form>
    <p> Hover for transaction destination/ origin. <br>
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
