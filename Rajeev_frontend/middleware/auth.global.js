import { useAuthStore } from '#imports'
import { defineNuxtRouteMiddleware, navigateTo } from '#imports'

export default defineNuxtRouteMiddleware((to) => {

  if (process.server) return
  try {
    const publicRoutes = ['/', '/register']
    const isPublicRoute = publicRoutes.includes(to.path)
    const auth = useAuthStore()

    try { auth.initFromStorage?.() } catch (e) { console.error('initFromStorage error', e) }
    if (!auth?.isAuthenticated && !isPublicRoute) {
      // Redirect to login with return URL
      return navigateTo(`/?next=${encodeURIComponent(to.fullPath)}`)
    }
  } catch (err) {

    console.error('auth middleware error:', err)
    return
  }
})