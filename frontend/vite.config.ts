import { fileURLToPath } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, fileURLToPath(new URL('..', import.meta.url)), '')
  return {
    plugins: [react()],
    server: {
      port: Number(env.FRONTEND_PORT || 3000),
      strictPort: true,
      proxy: {
        '/api': { target: `http://127.0.0.1:${env.BACKEND_PORT || 8000}` },
      },
    },
  }
})
