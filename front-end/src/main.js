import 'bootstrap/dist/css/bootstrap.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import gAuthPlugin from 'vue3-google-oauth2';

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
let gauthClientId = '1054307953063-2vrvhj18i99oadpqijvm7g98gvo72lat.apps.googleusercontent.com'

createApp(App).use(store).use(router, axios).use(gAuthPlugin, {clientId: gauthClientId,scope: 'profile email',prompt: 'select_account',}).mount('#app')

import 'bootstrap/dist/js/bootstrap.js'
