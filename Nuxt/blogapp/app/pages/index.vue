<template>
  <div class="page">
    <h1>Home Page</h1>
    <p>Welcome to the simple Nuxt app home page!</p>

    <NuxtLink to="/about" class="link">Go to About Page →</NuxtLink>
  </div>
</template>

<style scoped>
.page {
  text-align: center;
  margin-top: 100px;
  font-family: "Segoe UI", Roboto, sans-serif;
}

h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

p {
  color: #555;
  margin-bottom: 20px;
}

.link {
  display: inline-block;
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.3s ease;
}

.link:hover {
  background-color: #2980b9;
}
</style>
