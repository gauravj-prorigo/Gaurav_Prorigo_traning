<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1>Register</h1>

      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label>Username</label>
          <input v-model="form.username" type="text" required />
        </div>

        <div class="form-group">
          <label>Email</label>
          <input v-model="form.email" type="email" required />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input v-model="form.password" type="password" required minlength="6" />
        </div>

        <div class="form-group">
          <label>Role</label>
          <select v-model="form.role" required>
            <option disabled value="">Select Role</option>
            <option value="user">User</option>
            <option value="employee">Author</option>
            <option value="admin">Admin</option>
          </select>
        </div>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Registering...' : 'Register' }}
        </button>

        <p class="error" v-if="error">{{ error }}</p>
      </form>

      <p class="switch-text">
        Already have an account? <NuxtLink to="/">Login</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from '#imports'
import { useAuthStore } from '#imports'

const auth = useAuthStore()
auth.initFromStorage()

const router = useRouter()
const form = reactive({ username: '', email: '', password: '', role: '' })
const loading = ref(false)
const error = ref(null)

async function onSubmit() {
  if (!form.username || !form.email || !form.password || !form.role) {
    error.value = 'All fields are required.'
    return
  }

  loading.value = true
  error.value = null

  try {
    const res = await auth.register(form)
    if (res.tokens) router.push('/')
    else router.push('/index')
  } catch (err) {
    error.value = err?.data?.message || err?.message || 'Registration failed'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f6fa;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  background: #fff;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
  text-align: center;
  margin-bottom: 16px;
  color: #333;
}

.form-group {
  margin-bottom: 14px;
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
  font-weight: 500;
  color: #333;
}

input, select {
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

input:focus, select:focus {
  border-color: #007bff;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

button:disabled {
  background-color: #7aaef7;
  cursor: not-allowed;
}

.error {
  color: red;
  font-size: 0.9rem;
  text-align: center;
  margin-top: 10px;
}

.switch-text {
  text-align: center;
  margin-top: 12px;
  color: #333;
}

.switch-text a {
  color: #007bff;
  text-decoration: none;
}
option {
  background-color: #fff;
  color: #333;
  padding: 6px;
}

</style>
