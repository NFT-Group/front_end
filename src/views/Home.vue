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
        <option value="cryptokittens">CryptoPunks</option>
        <option value="boredapes">Bored Ape Yacht Club</option>
        <option value="boredapekennel">Bored Ape Kennel Club</option>
        <option value="doodles">Doodles</option>
        <option value="coolcats">Cool Cats</option>
        <option value="cryptoadz">CrypToadz</option>
        <option value="pudgypenguins">Pudgy Penguins</option>
        <option value="clonex">cloneX</option>
    </select>
    <br>
  </form>
  <div>
    <index />
  </div>

</template>

<script>
  import index from '@/components/index'
  export default
  {
      name: 'App',
      components: { index }
  }
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
