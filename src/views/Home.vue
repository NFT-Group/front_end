<template>

  <h1 class="title">Quantum</h1>
  <p>AN NFT MARKET ANALYSER AND VISUALISER</p>
  <br><br>
  <p class="input">EXPLORE...</p>
  <br><br>
  <div>
    <index />
    <!-- <index2 />  -->
  </div>

</template>

<script>
  import index from '@/components/index'
  import index2 from '@/components/index2'
  export default
  {
      name: 'App',
      components: { index, index2 }
  }
</script>

<style>
  h1.title{
    font-size: 50px;
  }
  p.input{
    color: #444; 
    font-size: 1.2em; 
  }

</style>
