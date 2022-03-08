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
    <h2>Select collection:</h2>
    <input type="radio" id="ape" name="collection" value="ape" checked="checked">
    <label for="ape">Bored Apes</label>
    <input type="radio" id="cryptoad" name="collection" value="cryptoad">
    <label for="cryptoad">CrypToadz</label>
    <input type="radio" id="punk" name="result_type" value="punk">
    <label for="punk">CryptoPunk</label><br><br>
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
      evt.preventDefault();
      console.log("entering onSubmit")
      const path = 'https://front-end-one-smoky.vercel.app/api/get_price';
      axios.get(path)
        .then((res) => {
          console.log(res)
          console.log(res.data)
          document.getElementById('nft_price_display').innerHTML=res.data["price"];
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
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
</style>
