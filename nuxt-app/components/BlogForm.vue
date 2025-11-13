<template>
  <form @submit.prevent="submit" class="blog-form">
    <input v-model="title" placeholder="Title" />
    <textarea v-model="content" rows="6" placeholder="Content"></textarea>

    <div class="controls">
      <button type="submit" class="btn-primary">{{ isEditing ? 'Save' : 'Publish' }}</button>
      <button v-if="isEditing" type="button" class="btn-ghost" @click="cancel">Cancel</button>
    </div>
  </form>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useBlogStore } from '~/stores/blogs'
import { useAuthStore } from '#imports'

const store = useBlogStore()
const auth = useAuthStore()
const config = useRuntimeConfig()

// local fields
const title = ref('')
const content = ref('')

// reactive getter for whether we are editing
const isEditing = computed(() => !!store.currentEdit)

// current edit object (reactive)
const currentEdit = computed(() => store.currentEdit) // store.currentEdit is a Pinia getter referencing editingBlog

// when the editing target changes, populate inputs (or clear if null)
watch(currentEdit, (val) => {
  if (val) {
    title.value = val.title ?? ''
    content.value = val.content ?? ''
  } else {
    title.value = ''
    content.value = ''
  }
}, { immediate: true })

// submit handler: create or update via store actions
const submit = async () => {
  const t = title.value.trim()
  const c = content.value.trim()
  if (!t || !c) return alert('Please provide title and content')

  try {
    if (isEditing.value && currentEdit.value?.id) {
      await store.updateBlog(config.public.apiBase, currentEdit.value.id, t, c)
    } else {
      await store.addBlog(config.public.apiBase, t, c)
    }
    // after success, store actions update blogs and clear editingBlog
    // clear local fields (safety)
    title.value = ''
    content.value = ''
  } catch (err) {
    console.error('submit error', err)
    alert('Save failed')
  }
}

// cancel editing
const cancel = () => {
  store.cancelEditing()
}
</script>

<style scoped>
.blog-form { display:block; max-width:720px; margin:0 auto; }
input, textarea {
  width:100%; padding:.6rem; border-radius:8px; border:1px solid #ddd; margin-bottom:.5rem; box-sizing:border-box;
}
.controls { display:flex; gap:.5rem; justify-content:flex-end; margin-top:.5rem; }
.btn-primary { background: linear-gradient(90deg,#667eea,#764ba2); color:#fff; border:none; padding:.5rem .8rem; border-radius:8px; cursor:pointer;}
.btn-ghost { background:transparent; border:1px solid #ddd; padding:.45rem .75rem; border-radius:8px; cursor:pointer;}
</style>
