import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { Grid } from "gridjs";
import "gridjs/dist/theme/mermaid.css";
import { GridGlobal } from 'gridjs-vue'
Vue.use(GridGlobal)
//import * as d3 from 'd3'
//import * as firebase from 'firebase'
//import * as Charts from './charts/charts.js'
createApp(App).use(router).mount('#app')
