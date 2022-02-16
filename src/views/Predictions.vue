<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
  <script src="https://www.gstatic.com/firebasejs/9.0.2/firebase-app-compat.js"></script> 
  <script src="https://www.gstatic.com/firebasejs/9.0.2/firebase-firestore-compat.js"></script>
      
  <script type="module"></script>
      <script>
      // Firebase web app configuration
      const firebaseConfig = {
        apiKey: "AIzaSyCMbegkc1LAvlUpj2akUiBr_I9lB2OW19k",
        authDomain: "practice-firebase-52292.firebaseapp.com",
        projectId: "practice-firebase-52292",
        storageBucket: "practice-firebase-52292.appspot.com",
        messagingSenderId: "481429582032",
        appId: "1:481429582032:web:de4d582b032c9d8ad6eed5",
        measurementId: "G-QBXC1HV2C0"
      };

      //Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      const db = firebase.firestore();

  </script>
  <script src="https://d3js.org/d3.v7.min.js"></script> 
  <script src="firebase_index.js"></script>
</script>