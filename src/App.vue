<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/predictions">Predictions</router-link> |
    <router-link to="/whalewatch">Whale Watch</router-link> |
    <router-link to="/about">About</router-link>
  <router-view/>
  <index />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased; */ /* this has been causing errors for some reason? */
  /* -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color:midnightblue;
}


p{
  color: #666e77;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #2c7453;
}

button{
  margin: 0 10px; 
  padding: 10px; 
  border: none; 
  border-radius: 4px; 
}
</style>
