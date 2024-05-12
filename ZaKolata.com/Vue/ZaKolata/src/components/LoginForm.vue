<template>
    <div id="loginForm" v-if="showLogin">
        <form @submit.prevent="submitForm" class="form">
            <div class="login-text">
                <h2>Login</h2>
                <img :src="logo" alt="">
            </div>
            <div class="input-div">
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="cr.username" required>
            </div>
            <div class="input-div">
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="cr.password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
    import logoImg from '@/assets/imgs/logo.png'; // '@' is an alias to /src in Vue CLI
    import { EventBus } from '@/event-bus.js';

    export default {
        data() {
            return {
                cr: {
                    username: "",
                    password: "",
                },
                logo: logoImg,
                showLogin: false,
            }
        },
        created() {
            EventBus.on('user-func-showLogin', this.theMethod);
        },
        methods: {
            showLogin() {
                this.showLogin = true
            },
            submitForm() {
                console.log('Form submitted with:', this.cr);
                // Add your login logic here
            }
        },
        unmounted() {
            EventBus.off('user-func-showLogin', this.theMethod);
        }
    }
    
</script>

<style scoped>
    template {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    #loginForm {
        background: -webkit-linear-gradient(left, #ff07fb57, #007dee57);
        width: 300px;
        border-radius: 10px;
        padding-left: 10px;
        padding-top: 5px;
        padding-right: 10px;
        height: 200px;
    }

    .form {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    .login-text {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        gap: 20px;
    }

    .login-text img {
        height: 46px;
    }

    .login-text h2 {
        margin: 0;
        color: white;
    }

    .input-div {
        color: white;
        display: flex;
        gap: 10px;
        align-items: center;
    }

    .input-div input {
        background-color: rgba(70, 70, 70, 0.603);
        border: 1px solid white;
        border-radius: 10px;
        color: white;
    }
    button {
        width: 30%;
        padding-top: 5px;
        padding-bottom: 5px;
        background-color: #0000005c;
        border: 0px;
        border-radius: 5px;
        color: white;
        transition: background-color 0.2s linear;
    }
    button:hover {
        background-color: black;
    }
</style>