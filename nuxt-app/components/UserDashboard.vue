<template>
  <section class="user-dashboard">
    <div class="dashboard-grid">
      <!-- Profile Card -->
      <div class="profile-card">
        <div class="profile-header">
          <h2 class="profile-title">Profile</h2>
          <div class="profile-avatar">
            {{ getInitials(auth.user.username) }}
          </div>
        </div>
        <div class="profile-details">
          <div class="detail-item">
            <div class="detail-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <div class="detail-content">
              <span class="detail-label">Username</span>
              <span class="detail-value">{{ auth.user.username }}</span>
            </div>
          </div>
          <div class="detail-item">
            <div class="detail-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="detail-content">
              <span class="detail-label">Email</span>
              <span class="detail-value">{{ auth.user.email }}</span>
            </div>
          </div>
          <div class="detail-item">
            <div class="detail-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div class="detail-content">
              <span class="detail-label">Role</span>
              <span class="role-badge user">User</span>
            </div>
          </div>
        </div>
      </div>
      <BlogList/>
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

function excerpt(text = '', len = 200) { 
  return text.length > len ? text.slice(0, len) + '…' : text 
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
  padding: 0;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr 2fr;
  }
}

/* Profile Card Styles */
.profile-card {
    max-height: 400px;
  background: white;
  border-radius: 16px;
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.8);
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.profile-card:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.profile-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.profile-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}

.profile-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.1rem;
  backdrop-filter: blur(10px);
}

.profile-details {
  padding: 1.5rem;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 0;
  border-bottom: 1px solid #f1f5f9;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.detail-icon svg {
  width: 20px;
  height: 20px;
  color: #64748b;
}

.detail-content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex: 1;
}

.detail-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.detail-value {
  font-weight: 600;
  color: #1e293b;
  font-size: 0.95rem;
}

.role-badge {
  padding: 0.375rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: inline-block;
}

.role-badge.user {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}

/* Blogs Card Styles */
.blogs-card {
  background: white;
  border-radius: 16px;
  box-shadow: 
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.8);
  overflow: hidden;
}

.card-header {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1.5rem;
  border-bottom: 1px solid #f1f5f9;
}

@media (min-width: 640px) {
  .card-header {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
  }
}

.card-title-section {
  flex: 1;
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0 0 0.25rem 0;
}

.card-subtitle {
  font-size: 0.875rem;
  color: #64748b;
  margin: 0;
}

/* Button Styles */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  text-decoration: none;
  line-height: 1;
  white-space: nowrap;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none !important;
}

.btn:focus {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

.btn-primary {
  background: #3b82f6;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.3);
}

.btn-content,
.btn-loading {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.refresh-icon {
  width: 1.25rem;
  height: 1.25rem;
  flex-shrink: 0;
}

/* Loading States */
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
  width: 24px;
  height: 24px;
  border: 2px solid transparent;
  border-top: 2px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

.spinner.large {
  width: 32px;
  height: 32px;
  border-width: 3px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .profile-card,
  .blogs-card {
    background: #1e293b;
    border-color: #334155;
  }
  
  .profile-header {
    background: linear-gradient(135deg, #4f46e5 0%, #7e22ce 100%);
  }
  
  .detail-icon {
    background: #334155;
  }
  
  .detail-icon svg {
    color: #94a3b8;
  }
  
  .detail-value {
    color: #f1f5f9;
  }
  
  .role-badge.user {
    background: #334155;
    color: #cbd5e1;
    border-color: #475569;
  }
  
  .card-title {
    color: #f1f5f9;
  }
  
  .card-subtitle {
    color: #94a3b8;
  }
  
  .detail-item {
    border-bottom-color: #334155;
  }
  
  .card-header {
    border-bottom-color: #334155;
  }
}

/* Responsive adjustments */
@media (max-width: 767px) {
  .profile-header {
    padding: 1rem;
  }
  
  .profile-details {
    padding: 1rem;
  }
  
  .detail-item {
    padding: 0.75rem 0;
  }
  
  .card-header {
    padding: 1rem;
  }
  
  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>