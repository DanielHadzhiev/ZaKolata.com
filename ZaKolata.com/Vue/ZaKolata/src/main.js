import Home from './views/Home.vue'
import Products from './views/Products.vue'
import ProductInfo from './views/ProductInfo.vue'

import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import axios from 'axios'; // for communication to backend

//base url backend
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

const router = createRouter({
    history: createWebHistory(), // This replaces mode: 'history'
    routes: [{
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/products',
            name: 'products',
            component: Products
        },
        {
            path: '/products/:id',
            name: 'productInfo',
            component: ProductInfo,
            props: true
        }
    ]
});

const app = createApp(App);
app.config.globalProperties.$axios = axios;
app.use(router);
app.mount('#app');