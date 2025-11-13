<template>
  <section>
    <div class="grid md:grid-cols-3 gap-6 mb-6">
      <div class="md:col-span-1 bg-white p-4 rounded shadow">
        <h2 class="font-semibold mb-2">Profile</h2>
        <p><strong>Username:</strong> {{ auth.user.username }}</p>
        <p><strong>Email:</strong> {{ auth.user.email }}</p>
        <p><strong>Role:</strong> <span class="badge">Employee</span></p>
      </div>

      <div class="md:col-span-2 bg-white p-4 rounded shadow">
        <!-- <div class="flex items-center justify-between mb-3">
          <h3 class="font-semibold">My Blogs</h3>
          <div>
            <button class="btn" @click="openEditor(null)">New Blog</button>
            <button class="btn ml-2" @click="fetchMyBlogs">Refresh</button>
          </div>
        </div> -->

        <div v-if="loading" class="text-sm text-slate-500">Loading...</div>
        <!-- <div v-else>
          <div v-if="blogs.length === 0" class="text-slate-500">No blogs yet.</div>
          <div v-for="b in blogs" :key="b.id" class="p-3 border rounded mb-3 flex justify-between">
            <div>
              <h4 class="font-semibold">{{ b.title }}</h4>
              <p class="text-xs text-slate-400">Created: {{ formatDate(b.created_at) }}</p>
              <p class="mt-2 text-slate-700">{{ excerpt(b.content) }}</p>
            </div>
            <div class="flex gap-2">
              <button class="btn" @click="openEditor(b)">Edit</button>
              <button class="btn-danger" @click="deleteBlog(b)">Delete</button>
            </div>
          </div>
        </div> -->
      </div>
    </div>
      <BlogList />
    <!-- <BlogForm v-if="editorOpen" :blog="editing" @close="closeEditor" @saved="onSaved" /> -->
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '#imports'
import BlogForm from '~/components/BlogForm.vue'

const auth = useAuthStore()
const API_BASE = 'http://127.0.0.1:8000'

const blogs = ref([])
const loading = ref(false)

const editorOpen = ref(false)
const editing = ref(null)

onMounted(() => { fetchMyBlogs() })

async function fetchMyBlogs() {
  loading.value = true
  try {
    const res = await fetch(`${API_BASE}/api/blogs/`, {
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    const data = await res.json()
    console.log('raw blogs:', data)

    const arr = Array.isArray(data) ? data : []
    blogs.value = arr.filter(b => {
      if (!b) return false
      // authorId will be either b.author.id (if object) or b.author (if number)
      const authorId = b?.author?.id ?? b?.author
      return Number(authorId) === Number(auth.user?.id)
    })

    console.log('my blogs after filter:', blogs.value)
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}


function openEditor(blog) { editing.value = blog ? { ...blog } : null; editorOpen.value = true }
function closeEditor() { editorOpen.value = false; editing.value = null }
function onSaved() { closeEditor(); fetchMyBlogs() }

function excerpt(text = '', len = 160) { return text.length > len ? text.slice(0, len) + '…' : text }
function formatDate(dt) { return dt ? new Date(dt).toLocaleString() : '-' }

async function deleteBlog(blog) {
  if (!confirm('Delete this blog?')) return
  try {
    await fetch(`${API_BASE}/api/blogs/${blog.id}/`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${auth.token}` }
    })
    fetchMyBlogs()
  } catch (e) { console.error(e) }
}
</script>

<style scoped>
.btn { background:#10b981;color:white;padding:6px 10px;border-radius:8px;font-weight:600 }
.btn-danger { background:#ef4444;color:white;padding:6px 10px;border-radius:8px;font-weight:600 }
.badge { background:#f1f5f9;padding:2px 8px;border-radius:999px;font-size:12px }
</style>
