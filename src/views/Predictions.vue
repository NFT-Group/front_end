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
  <h2 id="testheader">Curate your own NFT...</h2>
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
  methods: {
    onSubmit() {
      console.log("entering onSubmit")
      const path = 'https://front-end-one-smoky.vercel.app/get_price';
      axios.post(path)
        .then((res) => {
          console.log("inside axios.post")
          console.log(res)
          console.log(res.data)
          document.getElementById('testheader').innerHTML=res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log("error onSubmit")
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
