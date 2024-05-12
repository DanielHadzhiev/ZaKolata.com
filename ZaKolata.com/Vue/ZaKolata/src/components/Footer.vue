<template>
    <div>
        <h2>КОНТАКТИ</h2>
        <div class="footer-info">
            <img :src="logoImg" alt="" class="f-img">
            <div class="line"></div>
            <div class="icons">
                <a href=""><i class="fa fa-phone" aria-hidden="true"></i></a>
                <a href=""><i class="fa fa-instagram" aria-hidden="true"></i></a>
                <a href=""><i class="fa fa-facebook" aria-hidden="true"></i></a>
                <a href=""><i class="fa fa-times" aria-hidden="true"></i></a>
            </div>
        </div>
        <p>© 2024 - ZaKolata - All Rights Reserved.</p>
    </div>
</template>

<script>
    import logo from '@/assets/imgs/logo.png'

    export default {
        data() {
            return {
                logoImg: logo,
            }
        }
    }
</script>

<style scoped>
div {
    height: 200px;
    background-color: rgb(43, 43, 43);
}

div h2 {
    margin: 0;
    text-align: center;
    color: white;
}

.f-img {
    height: 75px;
}

.footer-info {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 20px;
}

.vr-f {
    color: white;
}

.footer-info a {
    font-size: 255%;
    text-decoration: none;
    color: white;
    transition: color 0.5s linear;
}

.footer-info a:hover {
    background: -webkit-linear-gradient(left, #ff07fb, #007dee);
    /* Gradient from red to blue */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}

.icons {
    height: 45px;
    display: flex;
    flex-direction: row;
    gap: 10px;
}

div p {
    color: rgb(106, 106, 106);
    margin: 0;
    text-align: center;
}
</style>

