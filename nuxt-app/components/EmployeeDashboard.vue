<template>
  <section class="employee-dashboard">
    <div class="dashboard-grid">
      <!-- Profile Section -->
      <div class="profile-section">
        <div class="profile-card">
          <div class="profile-header">
            <div class="profile-avatar">
              {{ getInitials(auth.user.username) }}
            </div>
            <div class="profile-info">
              <h2 class="profile-name">{{ auth.user.username }}</h2>
              <span class="profile-role">Employee</span>
            </div>
          </div>
          
          <div class="profile-details">
            <div class="detail-item">
              <span class="detail-label">Username:</span>
              <span class="detail-value">{{ auth.user.username }}</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Email:</span>
              <span class="detail-value">{{ auth.user.email }}</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Role:</span>
              <span class="role-badge">Employee</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Blogs Section -->
      <div class="blogs-section">
        <div class="blogs-header">
          <h2 class="blogs-title">My Blogs</h2>
          <button class="btn btn-primary" @click="showBlogForm = true">
            <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
            </svg>
            Create Post
          </button>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading-state">
          <div class="spinner"></div>
          <p>Loading your blogs...</p>
        </div>

        <!-- Blog List -->
        <div v-else class="blogs-content">
          <BlogList />
        </div>
      </div>
    </div>

    <!-- Blog Form Modal -->
    <BlogForm v-if="showBlogForm" @close="showBlogForm = false" @saved="onBlogSaved" />
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '#imports'
import BlogForm from '~/pages/BlogForm.vue'
import BlogList from '~/components/BlogList.vue'

const auth = useAuthStore()
const API_BASE = 'http://127.0.0.1:8000'

const blogs = ref([])
const loading = ref(false)
const showBlogForm = ref(false)

onMounted(() => { 
  fetchMyBlogs() 
})

async function fetchMyBlogs() {
  loading.value = true
  try {
    const res = await fetch(`${API_BASE}/api/blogs/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    const data = await res.json()
    console.log('raw blogs:', data)

    const arr = Array.isArray(data) ? data : []
    const myBlogs = arr.filter(b => {
      if (!b) return false
      const authorId = b?.author?.id ?? b?.author
      return Number(authorId) === Number(auth.user?.id)
    })

    blogs.value = myBlogs
    console.log('my blogs after filter:', blogs.value)
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

function onBlogSaved() {
  showBlogForm.value = false
  fetchMyBlogs()
}

function getInitials(username) {
  if (!username) return '??'
  return username
    .split(' ')
    .map(name => name.charAt(0))
    .join('')
    .toUpperCase()
    .substring(0, 2)
}
</script>

<style scoped>
.employee-dashboard {
  padding: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

/* Main Grid Layout */
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 1024px) {
  .dashboard-grid {
    grid-template-columns: 350px 1fr;
  }
}

/* Profile Section */
.profile-section {
  height: fit-content;
}

.profile-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid #e2e8f0;
  overflow: hidden;
}

.profile-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #4f46e5 0%, #7e22ce 100%);
  color: white;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.profile-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.25rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.profile-info {
  flex: 1;
}

.profile-name {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 0.25rem 0;
}

.profile-role {
  font-size: 0.875rem;
  opacity: 0.9;
  font-weight: 500;
}

.profile-details {
  padding: 1.5rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid #f1f5f9;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-label {
  font-size: 0.875rem;
  color: #64748b;
  font-weight: 500;
}

.detail-value {
  font-weight: 600;
  color: #1e293b;
  font-size: 0.95rem;
}

.role-badge {
  background: #f1f5f9;
  color: #475569;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Blogs Section */
.blogs-section {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid #e2e8f0;
  overflow: hidden;
}

.blogs-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #f1f5f9;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.blogs-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.blogs-content {
  padding: 0;
}

/* Button Styles */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.625rem 1rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  line-height: 1;
  white-space: nowrap;
}

.btn:focus {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

.btn-primary {
  background: #3b82f6;
  color: white;
}

.btn-primary:hover {
  background: #2563eb;
  transform: translateY(-1px);
}

.btn-icon {
  width: 1.125rem;
  height: 1.125rem;
  flex-shrink: 0;
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #64748b;
  text-align: center;
}

.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #f1f5f9;
  border-top: 3px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .employee-dashboard {
    padding: 0.75rem;
  }
  
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 0.75rem;
    padding: 1.25rem;
  }
  
  .blogs-header {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
  
  .blogs-header .btn {
    width: 100%;
    justify-content: center;
  }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
  .profile-card,
  .blogs-section {
    background: #1e293b;
    border-color: #334155;
  }
  
  .detail-value,
  .blogs-title {
    color: #f1f5f9;
  }
  
  .detail-label {
    color: #94a3b8;
  }
  
  .detail-item {
    border-bottom-color: #334155;
  }
  
  .blogs-header {
    border-bottom-color: #334155;
  }
  
  .role-badge {
    background: #334155;
    color: #cbd5e1;
  }
}
</style>