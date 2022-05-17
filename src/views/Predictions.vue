<template>
  <br><br>
  <center><div id="logo">
    <img src="../assets/images/Predictor.png"/>
  </div></center>
<h2>Price prediction </h2>
<p> Enter the collection and token ID of the NFT of interest. <br>
    A predicted value will be generated, along with a list of the NFT's attributes and their rarity relative to their collection. <br>
    The mean average percentage error is between 0.25 - 1.5% across the collections, suggesting 98.5% accuracy or greater on average.<br>
    <br>
    Note: Image loading will not work on Imperial Wi-Fi, since IPFS is blocked by Imperial<br> </p>
  <br>
  <img src="" id="nft_img">
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
  <h3 id="nft_price_display"></h3>
  <h4 id="nft_traits_display"></h4>
  <br><br><br><br>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Predictions',
  created() {
    
  },
  methods: {
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    onSubmit(evt) {
      var collection = evt.srcElement.collection.value
      var tokenid = evt.srcElement.tokenid.value
      var query_object = {"collection": collection, "tokenid": tokenid}
      evt.preventDefault();
      const path = 'https://nft-back-end-py.herokuapp.com/';
      axios.post(path, JSON.stringify(query_object), { headers: { 'content-type': 'text/json' }})
        .then((res) => {
          var ethPrice = (Math.round(res.data['price'] * 100)/ 100).toFixed(2)
          var gbpPrice = (Math.round((res.data['gbpprice'] * ethPrice)* 100)/ 100).toFixed(2)
          document.getElementById('nft_price_display').innerHTML = 'Predicted value: ' + ethPrice + ' ETH (£' + this.numberWithCommas(gbpPrice) + ')';
          // document.getElementById('nft_traits_display').innerHTML = res.data['attributes'];

          var attributeCount = 0;
          var startBrackets = [];
          var endBrackets = [];
          for (var i = 0; i < res.data['attributes'].length; i++) {
            if(res.data['attributes'][i] == '}') {
              endBrackets.push(i);
              attributeCount++;
            }
            if(res.data['attributes'][i] == '{') {
              startBrackets.push(i);
            }
          }
          
          var attributesList = []
          for(var i = 0; i < attributeCount; i++) {
            var substring = res.data['attributes'].substring(startBrackets[i], endBrackets[i] + 1)
            var substring2 = substring.replace(/'/g, '"')
            attributesList.push(substring2)
          }

          var JSONList = []
          for(var i = 0; i < attributesList.length; i++) {
            var jsonObject = JSON.parse(attributesList[i]) 
            JSONList.push(jsonObject)
          }

          for(var i = 0; i < JSONList.length; i++) {
            var object = JSONList[i];
            var attributeDescription = attributeDescription + "Attribute #" + (i + 1) + ": <br>"
            for (var key in object) {
              var value = object[key];
              if(key == 'trait_type') {
                attributeDescription += value + " : "
              } else if(key == 'value'){
                attributeDescription += value
              } else if(key == 'rarity') {
                value = 1 - value;
                value *= 100;
                var rarityString = value.toFixed(2);
                attributeDescription += " (Rarity: " + rarityString + "%)<br>"
              }
            }
            attributeDescription += "<br>"
          }
          var processedDescription = attributeDescription.replace('undefined', "")
          document.getElementById('nft_traits_display').innerHTML = processedDescription

          var link = res.data['ipfs']
          if(collection == "punk") {
            link = "http://media.raritysniper.com/cryptopunks/" + tokenid.toString() + "-600.png"
          } else if (link.substring(0, 4) == 'ipfs')
          {
            
            link = 'https://ipfs.io/ipfs/' + link.substring(7);
          }
          document.getElementById('nft_img').src=link
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
  img{
    max-width: 400px;
    max-height: 600px;
    width: auto;
    height: auto;
  }
  h2{
    color: #666e77;
    font-weight: 500;
  }
  h3{
    color: black;
    font-weight: 700;
  }
  h4{
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
  #logo {
    height: 120px;
    width: 190px; 
    text-align: center;
    display: flex;
  }
  #logo > img{
    text-align: center;
    max-width: 100%;
    max-height: 100%;
  }
</style>
