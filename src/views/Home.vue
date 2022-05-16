<template>
  <br><br>
  <center><div id="logo">
    <img src="../assets/images/Home.png"/>
  </div></center>
  <br><br>
  <div>
    <MultiLine/>
  </div>
  <br>
  <div>
    <MultiLine2/>
  </div>
  <br><br>
  <div>
    <chart/>
  </div>
  <br><br>
  <p class="input">Contact us</p>
  <br><br>
  <p> Enter your email and a message here. Our team will get back to you ASAP.</p>
  <form @submit.prevent="handleSubmit">
      <label>Enter your email:</label>
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
import MultiLine from '../components/MultiLine.vue'
import MultiLine2 from '../components/MultiLine2.vue'
  export default{
    name: 'App',
    components: { Chart,
                  MultiLine,
		              MultiLine2
    },
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
      },
      refreshing(){
        console.log('refreshing the bar chart')
      }
    }
  }
  
</script>

<style>
  h1.title{
    font-size: 50px;
  }
  h2{
    color: #666e77;
    font-weight: 500;
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
    text-align: center; 
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
    display: inline; 
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