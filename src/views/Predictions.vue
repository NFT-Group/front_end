<template>
  <h1>Price Predictor</h1>
  <br><br>
  <h2>Predict the value of your next NFT</h2>
  <br>
  <form @submit="onSubmit">
    <label>Enter a Collection:</label>
      <select value="collection" id="collection" name="collection">
          <option value="punk" id="punk" name="collection">CryptoPunks</option>
          <option value="boredape" id="boredape" name="collection">Bored Ape Yacht Club</option>
          <option value="boredapekennel" id="boredapekennel" name="collection">Bored Ape Kennel Club</option>
          <option value="doodle" id="doodle" name="collection">Doodles</option>
          <option value="coolcat" id="coolcat" name="collection">Cool Cats</option>
          <option value="cryptoad" id="cryptoad" name="collection">CrypToadz</option>
          <option value="penguin" id="penguin" name="collection">Pudgy Penguins</option>
          <option value="clonex" id="clonex" name="collection">cloneX</option>
      </select>
    <br><br>
    <label>Enter a Token ID:</label>
    <input type="number" required v-model="tokenID" id="tokenid" name="tokenid"> 
    <br><br>
    <input type="submit" name="submit_button">
  </form>
  <br><br>
  <h3 id="nft_price_display">Your NFT price will appear here... </h3>
  <br><br>
  <hr class="solid">
  <br><br>
  <h2 >Curate your own NFT</h2>
  <form @submit="onSubmit2">
    <label>Enter a Collection:</label>
      <select value="collection" id="collection" name="collection">
          <option value="punk" id="punk" name="collection">CryptoPunks</option>
          <option value="boredape" id="boredape" name="collection">Bored Ape Yacht Club</option>
          <option value="boredapekennel" id="boredapekennel" name="collection">Bored Ape Kennel Club</option>
          <option value="doodle" id="doodle" name="collection">Doodles</option>
          <option value="coolcat" id="coolcat" name="collection">Cool Cats</option>
          <option value="cryptoad" id="cryptoad" name="collection">CrypToadz</option>
          <option value="penguin" id="penguin" name="collection">Pudgy Penguins</option>
          <option value="clonex" id="clonex" name="collection">cloneX</option>
      </select>
    <br><br>
    <label>Enter a Token ID:</label>
    <input type="number" required v-model="tokenID" id="tokenid" name="tokenid"> 
    <br><br>
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
      var collection = evt.srcElement.collection.value
      var tokenid = evt.srcElement.tokenid.value
      console.log("collection")
      console.log(collection)
      console.log("tokenid")
      console.log(tokenid)
      var query_object = {"collection": collection, "tokenid": tokenid}
      console.log(query_object)
      //console.log(evt.srcElement.collection.value)
      //var collection_value = evt.srcElement.collection.value
      evt.preventDefault();
      console.log("entering onSubmit")
      const path = 'https://front-end-one-smoky.vercel.app/api/get_price';
      console.log(JSON.stringify(query_object))
      axios.post(path, JSON.stringify(query_object), { headers: { 'content-type': 'text/json' }})
        .then((res) => {
          console.log(res)
          console.log(res.data)
          document.getElementById('nft_price_display').innerHTML=res.data["price"];
        })
        .catch((error) => {
           //eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit2(evt) {
      console.log(evt);
      console.log("which element is checked?")
      var collection = evt.srcElement.collection.value
      var tokenid = evt.srcElement.tokenid.value
      console.log("collection")
      console.log(collection)
      console.log("tokenid")
      console.log(tokenid)
      var query_object = {"collection": collection, "tokenid": tokenid}
      console.log(query_object)
      //console.log(evt.srcElement.collection.value)
      //var collection_value = evt.srcElement.collection.value
      evt.preventDefault();
      console.log("entering onSubmit")
      const path = 'https://pgm21-simplewebapp.herokuapp.com/';
      console.log(JSON.stringify(query_object))
      axios.post(path, JSON.stringify(query_object), { headers: { 'content-type': 'text/json' }})
        .then((res) => {
          console.log(res)
          console.log(res.data)
          document.getElementById('nft_price_display').innerHTML=res.data;
        })
        .catch((error) => {
           //eslint-disable-next-line
          console.error(error);
        });
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