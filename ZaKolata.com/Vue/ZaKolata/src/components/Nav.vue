<template>
    <nav>
        <img :src="logo" alt="">
        <div class="btns" v-if="!isLogin">
            <a href="" @click.prevent="showLogin">Login</a>
            <a href="">Register</a>
        </div>
    </nav>
</template>


<script>
    import logoImg from '@/assets/imgs/logo.png'; // '@' is an alias to /src in Vue CLI

    export default {
        props: ['isLogin'],
        data() {
            return {
                logo: logoImg,
            }
        },
        methods: {
            showLogin() {
                EventBus.$emit('user-func-showLogin');
            }
        }
    }
</script>

<style scoped>
    nav {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        background-color: black;
    }

    nav img {
        height: 56px;
    }

    nav a {
        text-decoration: none;
        background: -webkit-linear-gradient(left, #ff07fb87, #007dee87);
        color: white;
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 5px;
        padding-bottom: 7px;
        border-radius: 5px;
        transition: background 0.2s linear;
        transition: border 0.2s linear;
    }

    nav a:hover {
        background: transparent;
        border: solid 2px purple;
    }

    .btns {
        display: flex;
        flex-direction: row;
        gap: 10px;
    }
</style>