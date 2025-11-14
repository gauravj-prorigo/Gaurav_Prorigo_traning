<template>
  <div class="overlay">
    <form @submit.prevent="submit" class="blog-form">
      <input v-model="title" placeholder="Title" />
      <textarea v-model="content" rows="6" placeholder="Content"></textarea>

      <div class="controls">
        <button type="button" class="btn-cancel" @click="emitClose">Cancel</button>
        <button type="submit" class="btn-primary">Publish</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useBlogStore } from '~/stores/blogs'
const router = useRouter()
const store = useBlogStore()
const config = useRuntimeConfig()

// local fields
const title = ref('')
const content = ref('')

// submit handler: create new blog
const submit = async () => {
  const t = title.value.trim()
  const c = content.value.trim()
  if (!t || !c) return alert('Please provide title and content')

  try {
    await store.addBlog(config.public.apiBase, t, c)
    router.back() 
    // clear local fields
    title.value = ''
    content.value = ''
  } catch (err) {
    console.error('submit error', err)
    alert('Failed to create post')
  }
}

// cancel handler
const emit = defineEmits(['close'])

function emitClose() {
  emit('close')
}
</script>

<style scoped>
.overlay {
  position: fixed; inset: 0; display: flex; align-items: center; justify-content: center;
  background: rgba(2,6,23,0.5); z-index: 1000; padding: 16px;
}

.blog-form {
  background: white;
  max-width: 600px;
  width: 90%;
  margin: 20px;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

input, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 16px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 14px;
}

textarea {
  resize: vertical;
  min-height: 120px;
}

.controls {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.btn-primary {
  background: #2563eb;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.btn-primary:hover {
  background: #1d4ed8;
}

.btn-cancel {
  background: #6b7280;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.btn-cancel:hover {
  background: #4b5563;
}
</style>