// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database"
//import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDAknBXvM7ex96Ce7wDD2YycINv9OKF5Bw",
  authDomain: "allcollections-6e66c.firebaseapp.com",
  databaseURL: "https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "allcollections-6e66c",
  storageBucket: "allcollections-6e66c.appspot.com",
  messagingSenderId: "172666013576",
  appId: "1:172666013576:web:77d1e890e083e6067a9c3d",
  measurementId: "G-BRG341YEJB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);

//import { initializeApp } from 'firebase/app'
//import { getDatabase } from "firebase/database"

//const firebaseConfig = {
    //apiKey: "AIzaSyCMbegkc1LAvlUpj2akUiBr_I9lB2OW19k",
    //authDomain: "practice-firebase-52292.firebaseapp.com",
    //databaseURL: "https://practice-firebase-52292-default-rtdb.europe-west1.firebasedatabase.app",
    //projectId: "practice-firebase-52292",
    //storageBucket: "practice-firebase-52292.appspot.com",
    //messagingSenderId: "481429582032",
    //appId: "1:481429582032:web:de4d582b032c9d8ad6eed5",
    //measurementId: "G-QBXC1HV2C0"
//}

//const app = initializeApp(firebaseConfig)

// Get a reference to the database service
const db = getDatabase(app)

export {
    db
}