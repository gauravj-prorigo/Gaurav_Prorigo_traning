// middleware/auth.js
import { useAuthStore } from '#imports'
import { defineNuxtRouteMiddleware, navigateTo } from '#imports'

export default defineNuxtRouteMiddleware((to) => {
  // don't run auth check on server (no localStorage available)
  if (process.server) return

  const auth = useAuthStore()
  auth.initFromStorage()

  if (!auth.isAuthenticated) {
    return navigateTo(`/?next=${encodeURIComponent(to.fullPath)}`)
  }
})
