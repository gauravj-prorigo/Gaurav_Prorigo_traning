<template>
  <div class="home-bg">
    <div class="home">
      <h1>Welcome to My Todo App</h1>
      <p>
        This is a simple Vue app where you can create and manage your daily tasks.
        Click below to add a new task or open the form page to enter more details.
      </p>

      <div class="buttons">
        <router-link to="/task">
          <button class="add">Add Task</button>
        </router-link>

        <router-link to="/form">
          <button class="form">Go to Form</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      name: "Gaurav Jadhav"
    };
  }
};
</script>

<style scoped>
.home-bg {
  min-height: 100vh; /* make the div fill the screen */
  background-image: url('@/assets/subtle-cinematics-KEI-VNDi0_g-unsplash.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
 
  /* align-items: center; */
}

.home {
  max-width: 600px;
  height: 300px;
   margin-top: 60px;
  padding: 30px;
  text-align: center;
  background: rgba(255, 255, 255, 0.85); /* overlay for readability */
  border-radius: 12px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
}

h1 {
  color: #3498db;
  margin-bottom: 10px;
}

p {
  color: #333;
  margin-bottom: 30px;
  line-height: 1.6;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

button {
  padding: 12px 28px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.add {
  background-color: #e67e22;
  color: white;
}

.add:hover {
  background-color: #d35400;
}

.form {
  background-color: #27ae60;
  color: white;
}

.form:hover {
  background-color: #1e8449;
}
</style>
