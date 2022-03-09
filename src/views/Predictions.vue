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
          <option value="punk" id="punk" name="collection">CryptoPunks</option>
          <option value="ape" id="ape" name="collection">Bored Ape Yacht Club</option>
          <option value="kennel" id="kennel" name="collection">Bored Ape Kennel Club</option>
          <option value="doodle" id="doodle" name="collection">Doodles</option>
          <option value="coolcat" id="coolcat" name="collection">Cool Cats</option>
          <option value="cryptoad" id="cryptoad" name="collection">CrypToadz</option>
          <option value="penguin" id="penguin" name="collection">Pudgy Penguins</option>
          <option value="clonex" id="clonex" name="collection">cloneX</option>
      </select>
    <br><br>
    <label>Enter a Token ID:</label>
    <input type="number" required v-model="tokenID" id="tokenid"> 
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
      //console.log(evt.srcElement.collection.value)
      //var collection_value = evt.srcElement.collection.value
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
    color: #666e77;
    font-weight: 500;
  }
  h3{
    color: #666e77;
    font-weight: 500;
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
