<template>
    <div class="whalewatching">
        <h1>Whale Watching</h1>
    </div>
    <br><br><br><br>
    <p> What's hot?</p>
    <br><br><br><br>
    <hr class="solid">
    <p>Insert Node Graph</p>
    <br><br><br><br>
    <hr class="solid">
    <p>Live Updating Whales</p>
    <br><br><br><br>
	<grid :cols="cols" :rows="rows"></grid>
</template>

<script>
  //import Grid from 'gridjs-vue'

  //export default {
    //name: 'Cars',
    //components: {
      //Grid
    //},
    //data() {
      //return {
        //cols: ['Make', 'Model', 'Year', 'Color'],
        //rows: [
          //['Ford', 'Fusion', '2011', 'Silver'],
          //['Chevrolet', 'Cruz', '2018', 'White']
        //]
      //}
    //}
  //}
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
