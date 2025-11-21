<template>
  <!-- :key forces remount when route changes (helps SPA redirect -> fresh layout) -->
  <div class="auth-page">
    <div class="auth-card" role="region" >
      <h1 id="register-title">Create account</h1>

      <form @submit.prevent="onSubmit" class="form" >
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model.trim="form.username"
            autocomplete="username"
            required
            :class="{ invalid: fieldErrors.username }"
            @blur="validateField('username')"
            placeholder="Choose a username"
          />
          <p v-if="fieldErrors.username" class="field-error">{{ fieldErrors.username }}</p>
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            type="email"
            v-model.trim="form.email"
            autocomplete="email"
            required
            :class="{ invalid: fieldErrors.email }"
            @blur="validateField('email')"
            placeholder="you@example.com"
          />
          <p v-if="fieldErrors.email" class="field-error">{{ fieldErrors.email }}</p>
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <div class="relative">
            <input
              id="password"
              :type="showPassword ? 'text' : 'password'"
              v-model="form.password"
              autocomplete="new-password"
              required
              minlength="6"
              :class="{ invalid: fieldErrors.password }"
              @blur="validateField('password')"
              placeholder="At least 6 characters"
            />
            <button type="button" class="show-btn" @click="showPassword = !showPassword" :aria-pressed="showPassword">
              {{ showPassword ? 'Hide' : 'Show' }}
            </button>
          </div>
          <p v-if="fieldErrors.password" class="field-error">{{ fieldErrors.password }}</p>
        </div>

        <!-- NOTE: role selection removed — backend will set role = 'user' by default -->
        <div class="muted-note">
          New accounts are created as <strong>user</strong> by default. Admin will assign other roles later.
        </div>

        <button type="submit" :disabled="loading" class="btn-primary" aria-busy="loading">
          <span>{{ loading ? 'Creating account...' : 'Create account' }}</span>
        </button>
      </form>

      <p class="switch-text">
        Already have an account?
        <NuxtLink to="/login">Login</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue'
import { useRouter, useRoute } from '#imports'
import { useAuthStore } from '#imports'
definePageMeta({
  layout: 'public'
  // No middleware needed - handled globally
})
const auth = useAuthStore()
// restore store on client (safe)
if (process.client && typeof auth.initFromStorage === 'function') {
  auth.initFromStorage()
}

const router = useRouter()
const route = useRoute()

const form = reactive({
  username: '',
  email: '',
  password: ''
})

const loading = ref(false)
const error = ref(null)
const showPassword = ref(false)

const fieldErrors = reactive({
  username: null,
  email: null,
  password: null
})

function validateField(field) {
  fieldErrors[field] = null

  if (field === 'username') {
    if (!form.username || form.username.trim().length < 3) {
      fieldErrors.username = 'Enter username (min 3 chars).'
    }
  }

  if (field === 'password') {
    if (!form.password || form.password.length < 6) {
      fieldErrors.password = 'Password must be at least 6 characters.'
    }
  }
}

/**
 * Utility to flatten backend error objects/arrays into simple messages array
 * Accepts many common DRF error shapes: { field: ["err"] }, ["err"], "err"
 */
function flattenErrors(err) {
  if (!err) return []
  if (typeof err === 'string') return [err]
  if (Array.isArray(err)) return err.flatMap(e => (typeof e === 'string' ? e : JSON.stringify(e)))
  // object: collect values
  return Object.values(err).flatMap(v => (Array.isArray(v) ? v : [v])).map(String)
}

async function onSubmit() {
  // clear errors
  fieldErrors.username = null
  fieldErrors.email = null
  fieldErrors.password = null
  error.value = null

  // run validations
  validateField('username')
  validateField('password')

  if (fieldErrors.username || fieldErrors.email || fieldErrors.password) {
    error.value = 'Please fix the highlighted fields.'
    return
  }

  loading.value = true
  try {
    // 1) register user (backend sets role='user')
    const registerResponse = await auth.register({
      username: form.username,
      email: form.email,
      password: form.password
    })
    await auth.login({ username: form.username, password: form.password })

    const next = route.query.next ? decodeURIComponent(String(route.query.next)) : '/dashboard'
    await router.push(next)
  } catch (err) {
      error.value = 'Registration failed. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Page wrapper */
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url("https://e1.pxfuel.com/desktop-wallpaper/407/1022/desktop-wallpaper-website-backgrounds-login-page.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 24px;
  box-sizing: border-box;
}

/* Card */
.auth-card {
  width: 100%;
  max-width: 520px;
  background: linear-gradient(180deg, rgba(255,255,255,0.98), #ffffff);
  border-radius: 12px;
  padding: 26px;
  box-sizing: border-box;
  border: 1px solid rgba(20, 40, 80, 0.06);
  box-shadow: 0 10px 30px rgba(16,24,40,0.06);
}

/* Title */
h1 {
  margin: 0 0 8px;
  font-size: 1.4rem;
  color: #0b2545;
  text-align: left;
}

/* Info message shown when redirected */
.info {
  margin: 0 0 12px;
  color: #155724; /* greenish */
  background: #ecfdf5;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.95rem;
}

/* Form */
.form { display: grid; gap: 12px; margin-top: 6px; }

/* Form group */
.form-group { display: flex; flex-direction: column; gap: 6px; }

label {
  font-weight: 600;
  font-size: 0.95rem;
  color: #243b53;
}

/* Inputs */
input {
  padding: 10px 12px;
  border-radius: 8px;
  border: 1px solid #d6e6fb;
  background: #fbfdff;
  font-size: 0.95rem;
  outline: none;
  transition: border-color .12s ease, box-shadow .12s ease;
  width: 100%;
  box-sizing: border-box;
}

input:focus {
  border-color: #2b6cb0;
  box-shadow: 0 8px 22px rgba(43,108,176,0.06);
}

/* Show button */
.relative { position: relative; }
.show-btn {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: #475569;
  font-weight: 600;
  cursor: pointer;
}

/* Invalid input */
.invalid {
  border-color: #e53e3e !important;
}

/* Field error */
.field-error {
  color: #e53e3e;
  font-size: 0.88rem;
  margin-top: 4px;
}

/* Muted note */
.muted-note {
  font-size: 0.9rem;
  color: #475569;
  background: #f8fafc;
  padding: 8px 10px;
  border-radius: 8px;
  border: 1px solid #edf2f7;
}

/* Primary button */
.btn-primary {
  margin-top: 6px;
  width: 100%;
  padding: 10px 12px;
  border-radius: 10px;
  border: none;
  font-weight: 700;
  background: linear-gradient(90deg,#06b6d4,#3b82f6);
  color: white;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: transform .12s ease, opacity .12s ease;
}

.btn-primary[disabled] {
  opacity: 0.65;
  cursor: not-allowed;
  transform: none;
}

/* spinner */
.spinner {
  width: 16px;
  height: 16px;
  animation: spin 1s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* Server errors */
.server-error {
  margin-top: 8px;
  color: #7f1d1d;
  background: #fff1f2;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #fecaca;
  font-weight: 600;
}

/* Footer text */
.switch-text {
  margin-top: 12px;
  text-align: center;
  color: #334e68;
  font-size: 0.95rem;
}

.switch-text a {
  color: #1f6feb;
  text-decoration: none;
  font-weight: 700;
}

/* Small screens */
@media (max-width: 640px) {
  .auth-card { padding: 18px; border-radius: 8px; max-width: 420px; }
  input { padding: 10px; }
  .btn-primary { padding: 10px; border-radius: 8px; }
}
</style>
