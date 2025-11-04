<template>
  <div class="blog-page">
    <NuxtLink to="/" class="return-btn">← Return Home</NuxtLink>

    <h1>Blog Posts</h1>

    <div v-if="error" class="error">
      <p>Error loading posts: {{ error.message }}</p>
    </div>

    <div v-else-if="!posts || !posts.length" class="loading">
      <p>Loading posts...</p>
    </div>

    <div v-else class="posts">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Post {
  id: number 
  title: string
  content: string
}

const apiUrl = 'http://127.0.0.1:8000/add&viewblog/'
const { data: posts, error } = await useFetch<Post[]>(apiUrl)
</script>

<style scoped>
.blog-page {
  max-width: 800px;
  margin: 50px auto;
  font-family: "Segoe UI", Roboto, sans-serif;
  color: #2c3e50;
  padding: 0 20px;
}

.return-btn {
  display: inline-block;
  margin-bottom: 20px;
  padding: 8px 15px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.return-btn:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 2.5rem;
}

.posts {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.post-card {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 10px;
  background-color: #f9f9f9;
  transition: transform 0.2s, box-shadow 0.2s;
}

.post-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
}

.post-card h2 {
  margin-bottom: 10px;
  color: #3498db;
}

.post-card p {
  margin: 0;
  line-height: 1.6;
}

.loading,
.error {
  text-align: center;
  font-size: 1.2rem;
  color: #555;
}
</style>
