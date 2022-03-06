<template>
  <br><br>
  <hr class="solid">
  <p>Price Predictor:</p>
  <br><br><br><br>
  <p class="todo">INSERT CHECK BOX PRICE PREDICTION FEATURE</p>
  <div>
    <!-- <index2 /> -->
  </div>
  <br><br><br><br>
  <hr class="solid">
  <p>Curate your own NFT...</p>
  <br><br><br><br>
  <p class="todo">INSERT CHECK BOX CREATE YOUR OWN FEATURE</p>
  <br><br><br><br>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Predictions',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'https://front-end-one-smoky.vercel.app/predictions';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
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
