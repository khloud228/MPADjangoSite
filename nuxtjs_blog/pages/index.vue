<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12" justify-content-center>
        <div class="row my-4">
          <div v-for="post in posts" :key="post.slug" class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <img :src="post.image" alt="post-image" class="card-img-top">
              <div class="card-body">
                <h4 class="card-title">{{ post.title }}</h4>
                <p v-html="post.description" class="card-text"></p>
                <div class="d-flex justify-content-between align-items-center">
                  <nuxt-link to="#" class="btn btn-sm btn-outline-secondary">Подробнее</nuxt-link>
                  <small class="text-muted">{{ post.created_date }}</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'index',
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/posts/`)
    return {
      posts: data.results,
    }
  }
}
</script>
