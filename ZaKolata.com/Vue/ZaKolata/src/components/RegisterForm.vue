<template>
    <div id="loginForm" v-if="isShowingRegister">
        <form @submit.prevent="submitForm" class="form">
            <div class="login-text">
                <h2>Register</h2>
                <img :src="logo" alt="">
            </div>
            <div class="full-name">
                <div class="name-div">
                    <label for="username">First Name:</label>
                    <input type="text" id="first_name" v-model="cr.first_name" required placeholder="Име">
                </div>
                <div class="name-div">
                    <label for="username">Last Name:</label>
                    <input type="text" id="last_name" v-model="cr.last_name" required placeholder="Фамилия">
                </div>
            </div>
            <div class="input-div">
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="cr.username" required placeholder="Username">
            </div>
            <div class="input-div">
                <label for="username">Email:</label>
                <input type="text" id="email" v-model="cr.email" required placeholder="Email">
            </div>
            
            <div class="input-div">
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="cr.password" required placeholder="Парола">
            </div>
            <button type="submit">Register</button>
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
                    username: '',
                    email: '',
                    first_name: '',
                    last_name: '',
                    password: ''
                },
                logo: logoImg,
                isShowingRegister: false,
            }
        },
        created() {
            EventBus.on('user-func-showRegister', this.showRegister);
        },
        methods: {
            showRegister() {
                this.isShowingRegister = true
            },
            submitForm() {
                this.$axios.post('accounts/register', this.cr)
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that is not in the range of 2xx
                        console.log('Error data:', error.response.data);
                        console.log('Error status:', error.response.status);
                        console.log('Error headers:', error.response.headers);
                    } else if (error.request) {
                        // The request was made but no response was received
                        console.log('Error request:', error.request);
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        console.log('Error message:', error.message);
                    }
                    console.log(error.config); // Log request configuration
                });
                console.log('Form submitted with:', this.cr);
                // Add your login logic here
            }
        },
        unmounted() {
            EventBus.off('user-func-showRegister', this.showRegister);
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
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: auto; /* fixed width */
    height: auto; /* fixed height */
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

.full-name {
    display: flex;
    flex-direction: row;
    gap: 20px;
}

.name-div {
    color: white;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}

.name-div input {
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
    margin-bottom: 15px;
}
button:hover {
    background-color: black;
}
</style>