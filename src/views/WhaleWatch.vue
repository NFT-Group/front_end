<template>
  <br><br>
  <center><div id="logo">
    <img src="../assets/images/WhaleWatch.png">
  </div></center>
    <br>
    <div>
      <nodeChart/>
    </div>
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
  #logo {
    height: 120px;
    width: 190px; 
    text-align: center;
    display: flex;
  }
  #logo > img{
    text-align: center;
    max-width: 70%;
    max-height: 80%;
  }
</style>
