<template>

  <h1 class="title">Quantum</h1>
  <h2>AN NFT MARKET ANALYSER AND VISUALISER</h2>
  <br><br>
  <hr class="solid">
  <br><br>
  <div>
    <chart/>
  </div>
  <br><br>
  <hr class="solid">
  <p class="news">Latest News</p>
  <br><br>
  <hr class="solid">
  <p class="input">Contact us</p>
  <br><br>
  <p> Enter your email and a message here. Our team will get back to you ASAP.</p>
  <form @submit.prevent="handleSubmit">
      <label>Enter you email:</label>
      <input type="email" required v-model="emailInput">
      <label>Message:</label>
      <input type="text" required v-model="messageInput">
 
 <div class="submit">
   <button>Submit</button>
 </div>
 </form>
 
</template>

<script>
import Chart from '../components/Chart.vue'
  export default{
    name: 'App',
    components: { Chart },
    data(){
      return{
        emailInput: '',
        messageInput: '',
      }
    },
    methods:{
      handleSubmit(){
        console.log('form submitted')
        //at this point, submit result to database
      }
    }
  }
  
</script>

<style>
  h1.title{
    font-size: 50px;
  }
  p.input{
    color: #444; 
    font-size: 1.2em; 
  }
  hr.solid{
    border-top: 3px solid #bbb;
  }
  form{
    max-width: 420px; 
    margin: 30px auto; 
    background: white;
    text-align: left; 
    padding: 40px; 
    border-radius: 10px;  
    }
  label{
    color: #aaa; 
    display: inline-block; 
    margin: 25px 0 15px; 
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px; 
    font-weight: bold; 
  }
  input{
    display: block; 
    padding: 10px 6px; 
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd; 
    color: rgb(141, 138, 138); 
  }
  button{
    background: midnightblue;
    border: 0; 
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white;
    border-radius: 20px; 
  }
  .submit{
    text-align: center;
  }
</style>