<template>
    <section class="my-navigation">
        <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
            <div class="container-fluid">
                <nuxt-link class="navbar-brand" to="/"><img src="https://vectorified.com/images/gta-sa-icon-29.png" width="auto"
                        height="30" alt="GTA SA"></nuxt-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <div class="navbar-nav me-auto mb-2 mb-lg-0">
                        <nuxt-link class="nav-link active" aria-current="page" to="/">Главная</nuxt-link>
                        <nuxt-link class="nav-link" to="/contact">Контакты</nuxt-link>
                    </div>
                    <form class="d-flex p-1">
                        <input v-model="query" class="form-control me-2" placeholder="Поиск" aria-label="Search">
                        <button class="btn btn-outline-success me-2" type="submit" @click.stop.prevent="submit()">Искать</button>
                    </form>
                    <nuxt-link class="btn btn-outline-light me-2" to="/signup">Регистрация</nuxt-link>
                    <nuxt-link class="btn btn-outline-light me-2" to="/signin">Вход</nuxt-link>
                    <nuxt-link class="btn btn-outline-light me-2" to="/signout">Выход</nuxt-link>
                </div>
            </div>
        </nav>
    </section>
</template>

<script>
export default {
    name: 'Navbar',
    data() {
        return {
            query: null
        }
    },
    methods: {
        submit() {
            this.$router.push('/search?query=' + this.query)
        }
    }
}
</script>