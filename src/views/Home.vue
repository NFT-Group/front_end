<template>

  <h1>Quantum</h1>
  <p>AN NFT MARKET ANALYSER AND VISUALISER</p>
  <br><br>
  <p class="input">EXPLORE...</p>
  <form>
    <label>Blockchain:</label>
    <select >
        <option value="ethereum">Ethereum</option>
        <option value="solana">Solana</option>
    </select>
    <br>
    <label>Collection:</label>
    <select>
        <option value="allcollections">All Collection</option>
        <option value="cryptokittens">Crypto Kittens</option>
        <option value="boredapes">Bored Apes Yacht Club</option>
        <option value="littlelemon">Little Lemon</option>
        <option value="doodles">Doodles</option>
        <option value="artblocks">Art Blocks</option>
        <option value="cryptopunks">Crypto Punks</option>
        <option value="pudgypenguins">Pudgy Penguins</option>
        <option value="thesandbox">The Sandbox</option>
    </select>
    <br>
  </form>
</template>

<script>
//import index from '../components/index'

const charts = require('../charts/charts.js')
//import * as charts from '../charts/charts.js'

charts.barcharts()

//export default{
  //name: 'App',
  //components:{
    //index
  //},
//}
</script>


<style>
  form{
    max-width: 420px; 
    margin: 20px auto; 
    background: white; 
    text-align: left;
    padding: 0px;
    border-radius: 10px;
  }
  label{
    color:#aaa;
    display: inline-block;
    margin: 25px 0 15px; 
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px; 
    font-weight: bold; 
}
  input, select{
    display: block; 
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none; 
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  input[type="checkbox"]{
    display: inline-block;
    width: 16px; 
    margin: 0 10px 0 0; 
    position: relative; 
    top: 2px; 
  }
  p.input{
    color: #444; 
    font-size: 1.2em; 
  }

</style>
