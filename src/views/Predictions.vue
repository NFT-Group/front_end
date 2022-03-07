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
    onSubmit() {
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
