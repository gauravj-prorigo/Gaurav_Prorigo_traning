<template>
  <div class="page">
    <h1>About Page</h1>
    <p>This is a basic about page created with Nuxt.</p>

    <NuxtLink to="/" class="link">← Back to Home</NuxtLink>
  </div>
</template>

<style scoped>
.page {
  text-align: center;
  margin-top: 100px;
  font-family: "Segoe UI", Roboto, sans-serif;
}

h1 {
  color: #27ae60;
  margin-bottom: 10px;
}

p {
  color: #555;
  margin-bottom: 20px;
}

.link {
  display: inline-block;
  padding: 10px 20px;
  background-color: #27ae60;
  color: white;
  text-decoration: none;
  border-radius: 6px;

}

.link:hover {
  background-color: #1e8449;
}
</style>