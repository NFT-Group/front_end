<template>
  <br><br>
  <hr class="solid">
  <h2>Price Predictor:</h2>
  <br><br><br><br>
  <p class="todo">INSERT CHECK BOX PRICE PREDICTION FEATURE</p>
  <div>
    <!-- <index2 /> -->
  </div>
  <br><br><br><br>
  <hr class="solid">
  <h2 >Curate your own NFT...</h2>
  <h3 id="nft_price_display">Your NFT price will appear here... </h3>
  <br><br><br><br>
  <p class="todo">INSERT CHECK BOX CREATE YOUR OWN FEATURE</p>
  <form @submit="onSubmit">
    <label>Enter a Collection:</label>
      <select>
          <option value="cryptokittens">CryptoPunks</option>
          <option value="boredapes">Bored Ape Yacht Club</option>
          <option value="boredapekennel">Bored Ape Kennel Club</option>
          <option value="doodles">Doodles</option>
          <option value="coolcats">Cool Cats</option>
          <option value="cryptoadz">CrypToadz</option>
          <option value="pudgypenguins">Pudgy Penguins</option>
          <option value="clonex">cloneX</option>
      </select>
    <br><br>
    <label>Enter a Token ID:</label>
    <input type="number" required v-model="tokenID"> 
    <input type="submit" name="submit_button">
  </form>
  <br><br><br><br>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Predictions',
  created() {
    
  },
  methods: {
    onSubmit(evt) {
      console.log(evt);
      console.log("which element is checked?")
      console.log(evt.srcElement.collection.value)
      var collection_value = evt.srcElement.collection.value
      evt.preventDefault();
      console.log("entering onSubmit")
      const path = 'https://front-end-one-smoky.vercel.app/api/get_price';
      // axios.post(path, collection_value, { headers: { 'content-type': 'text/plain' }})
        //.then((res) => {
        //  console.log(res)
        //  console.log(res.data)
        //  document.getElementById('nft_price_display').innerHTML=res.data["price"];
        //})
       // .catch((error) => {
          // eslint-disable-next-line
        //  console.error(error);
       // });
    },
  },
};
</script>


<style>
  h2{
    font-size: 25px;
    color: black;
  }
  p.input{
    color: #444; 
    font-size: 1.2em; 
  }
  p.todo{
    font-style: italic;
  }
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
</style>
