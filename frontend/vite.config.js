import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// A configuração abaixo habilita a variável process no frontend
export default defineConfig({
  plugins: [vue()],
  define: {
    'process.env': {}, // Isso define a variável process.env para o frontend
  },
  server: {
    port: 5173, // Confirma que o servidor está rodando nessa porta
  }
})
