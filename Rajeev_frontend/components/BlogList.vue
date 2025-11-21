<template>
  <div class="blog-list">
    <h3>All Blogs</h3>

    <!-- Loading -->
    <div v-if="loading" class="loading">Loading blogs...</div>

    <!-- Empty -->
    <div v-else-if="blogs.length === 0" class="empty">No blogs found</div>

    <!-- Blog Items -->
    <div v-else>
      <div v-for="b in blogs" :key="b.id" class="blog-item">
        <div v-if="editingBlog?.id !== b.id">
          <h4>{{ b.title }}</h4>
          <p class="meta">
            By: @{{ authorName(b) }}
          </p>
          <p class="blog-description">{{ b.content }}</p>

          <div class="controls">
            <button v-if="canEdit(b)" class="btn-edit" @click="startEdit(b)">
              Edit
            </button>
            <button v-if="canDelete(b)" class="btn-delete" @click="deleteBlog(b)">
              Delete
            </button>
          </div>
          <p class="date">
            {{ formatDate(b.created_at) }}
          </p>
        </div>

        <!-- Inline Edit Form -->
        <div v-else class="edit-form">
          <input v-model="editTitle" placeholder="Title" />
          <textarea v-model="editContent" placeholder="Content"></textarea>

          <div class="form-actions">
            <button @click="updateBlog(b)">Save</button>
            <button class="cancel" @click="cancelEdit">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '#imports'
import { useToast } from 'vue-toastification'
const auth = useAuthStore()
const API_BASE = 'http://127.0.0.1:8000/api'
const toast = useToast()
const blogs = ref([])
const loading = ref(false)
const editingBlog = ref(null)
const editTitle = ref('')
const editContent = ref('')

/* ---------- Fetch Blogs ---------- */
async function fetchBlogs() {
  loading.value = true
  try {

    const res = await fetch(`${API_BASE}/blogs/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    if (!res.ok) throw new Error('Failed to fetch blogs') 
    const data = await res.json()
      blogs.value = data
    
  } catch (e) {
    console.error('fetchBlogs error', e)
  } finally {
    loading.value = false
  }
}
onMounted(fetchBlogs)

/* ---------- Permissions ---------- */
function getAuthorId(b) {
  return b?.author ?? null
}
function isOwner(b) {
  return Number(getAuthorId(b)) === Number(auth.user?.id)
}
function canEdit(b) {
  if (!auth.user) return false
  if (auth.hasRole('admin')) return true
  if (auth.hasRole('maneger')) return true
  if (auth.hasRole('employee') && isOwner(b)) return true
  return false
}
function canDelete(b) {
  if (!auth.user) return false
  if (auth.hasRole('admin')) return true
  if (auth.hasRole('employee') && isOwner(b)) return true
  if (auth.hasRole('maneger') && isOwner(b)) return true
}

/* ---------- Edit Handlers ---------- */
function startEdit(b) {
  editingBlog.value = b
  editTitle.value = b.title
  editContent.value = b.content
}
function cancelEdit() {
  editingBlog.value = null
  editTitle.value = ''
  editContent.value = ''
}

// Update blog
async function updateBlog(b) {
  try {
    const res = await fetch(`${API_BASE}/blogs/${b.id}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${auth.token}`
      },
      body: JSON.stringify({
        title: editTitle.value,
        content: editContent.value
      })
    })
    if (!res.ok) throw new Error('Update failed')
    toast.success('Blog Updated')
    const updated = await res.json()
    const idx = blogs.value.findIndex(x => x.id === b.id)
    if (idx !== -1) blogs.value[idx] = updated
    cancelEdit()
  } catch (e) {
    console.error('update error', e)
    alert('Failed to update blog')
  }
}

/* ---------- Delete ---------- */
async function deleteBlog(b) {
  try {
    const res = await fetch(`${API_BASE}/blogs/${b.id}/`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    if (!res.ok) throw new Error('Delete failed')
    toast.success('Blog Deleted')
    blogs.value = blogs.value.filter(x => x.id !== b.id)
  } catch (e) {
    console.error('delete error', e)
    alert('Failed to delete blog')
  }
}

/* ---------- Helpers ---------- */
function authorName(b) {
  return b?.author_username || `user#${b.author?.id ?? '-'}`
}
function formatDate(dt) {
  try {
    return new Date(dt).toLocaleString()
  } catch {
    return '-'
  }
}

</script>

<style scoped>
.blog-list {
  max-width: 1000px;
  margin: 0 auto;
}

.blog-item {
  border: 1px solid #e5e7eb;
  padding: 1rem 1rem 2.2rem;
  margin-bottom: 1rem;
  border-radius: 10px;
  background: #fff;
}

.blog-item {
  position: relative;
}

.controls {
  margin-top: 8px;
  display: flex;
  gap: 8px;
}

.btn-edit {
  background: #06b6d4;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
}

.btn-delete {
  background: #ef4444;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
}

.edit-form input,
.edit-form textarea {
  width: 100%;
  margin-bottom: 0.5rem;
  padding: 6px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

button.cancel {
  background: #9ca3af;
  color: white;
}

.date {
  position: absolute;
  right: 12px;
  bottom: 12px;
  font-size: 0.85rem;
  color: #6b7280;
}

/* Font and weight adjustments requested by user */
.blog-description {
  font-family: 'Knewave', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  font-size: 1rem;
  line-height: 1.3;
}

/* Make other visible text bold but keep their font-family unchanged */
.blog-item h4,
.blog-item .meta,
.blog-item p:not(.blog-description):not(.date),
.controls button,
.form-actions button {
  font-weight: 700;
}
</style>
