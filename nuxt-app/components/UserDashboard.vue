<template>
  <section class="user-dashboard">
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
              <span class="profile-role">User</span>
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
              <span class="role-badge">User</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Blog List Section -->
      <div class="blog-list-section">
        <BlogList />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '#imports'
import BlogList from './BlogList.vue'

const auth = useAuthStore()
const API_BASE = 'http://127.0.0.1:8000'

const blogs = ref([])
const loading = ref(false)

onMounted(() => { 
  fetchBlogs() 
})

async function fetchBlogs() {
  loading.value = true
  try {
    const res = await fetch(`${API_BASE}/api/blogs/`, { 
      headers: { Authorization: `Bearer ${auth.token}` } 
    })
    blogs.value = await res.json()
  } catch (e) { 
    console.error(e) 
  } finally { 
    loading.value = false 
  }
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
.user-dashboard {
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

@media (min-width: 768px) {
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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

/* Blog List Section */
.blog-list-section {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid #e2e8f0;
  overflow: hidden;
}

/* Responsive Design */
@media (max-width: 767px) {
  .user-dashboard {
    padding: 0.75rem;
  }
  
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 0.75rem;
    padding: 1.25rem;
  }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
  .profile-card,
  .blog-list-section {
    background: #1e293b;
    border-color: #334155;
  }
  
  .detail-value {
    color: #f1f5f9;
  }
  
  .detail-label {
    color: #94a3b8;
  }
  
  .detail-item {
    border-bottom-color: #334155;
  }
  
  .role-badge {
    background: #334155;
    color: #cbd5e1;
  }
}
</style>