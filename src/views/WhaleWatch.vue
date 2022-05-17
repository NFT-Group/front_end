<template>
  <br><br>
  <center><div id="logo">
    <img src="../assets/images/WhaleWatch.png">
  </div></center>
  <br>
  <div>
    <nodeChart/>
  </div>
  <br><br>
  <h2>Investigate individual transactions below:</h2> 
  <br>
  <!-- <grid :data="gridData" 
        :columns="gridColumns"></grid> -->
  <div>
    <Table/>
  </div>
  <br><br><br><br>
</template>

<script>
import NodeChart from '../components/NodeChart.vue'
import Table from "../components/Table.vue";


export default {
    name: "App",
    components: { 
      NodeChart,
      Table 
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
