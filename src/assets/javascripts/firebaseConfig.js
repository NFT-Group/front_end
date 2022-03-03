
import { initializeApp } from 'firebase/app'
import { getDatabase } from "firebase/database"

const firebaseConfig = {
    apiKey: "AIzaSyCMbegkc1LAvlUpj2akUiBr_I9lB2OW19k",
    authDomain: "practice-firebase-52292.firebaseapp.com",
    databaseURL: "https://practice-firebase-52292-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "practice-firebase-52292",
    storageBucket: "practice-firebase-52292.appspot.com",
    messagingSenderId: "481429582032",
    appId: "1:481429582032:web:de4d582b032c9d8ad6eed5",
    measurementId: "G-QBXC1HV2C0"
}

const app = initializeApp(firebaseConfig)

// Get a reference to the database service
const db = getDatabase(app)

export {
    db
}