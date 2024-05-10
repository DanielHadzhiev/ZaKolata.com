import Home from './Home.vue'
import Products from './Products.vue'
import ProductInfo from './ProductInfo.vue'

import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';


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
app.use(router);
app.mount('#app');