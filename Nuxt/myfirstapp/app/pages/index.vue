<template>
  <div class="page">
    <h1>Home Page</h1>
    <p>Welcome to the simple Nuxt app home page!</p>

    <div class="links">
      <NuxtLink to="/about" class="link">Go to About Page →</NuxtLink>
      <!-- <NuxtLink to="/counter" class="link">Go to Counter Page →</NuxtLink> -->
      <NuxtLink to="/task" class="link">Go to Task →</NuxtLink>
      <NuxtLink to="/blogapp" class="link">Go to Blog →</NuxtLink>
    </div>
  </div>
</template>

<style scoped>
.page {
  text-align: center;
  margin-top: 80px;
  font-family: "Segoe UI", Roboto, sans-serif;
  color: #2c3e50;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

p {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 30px;
}

.links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 15px;
}

.link {
  display: inline-block;
  padding: 12px 25px;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.link:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
