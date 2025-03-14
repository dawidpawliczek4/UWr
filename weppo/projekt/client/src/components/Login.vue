<template>
    <div>
      <h1>Logowanie</h1>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="email">Email:</label>
          <input id="email" type="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Hasło:</label>
          <input id="password" type="password" v-model="password" required />
        </div>
        <button type="submit">Zaloguj</button>
      </form>
      <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import axios from 'axios'
  
  const email = ref('')
  const password = ref('')
  const errorMessage = ref('')
  
  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:3000/auth/login', {
        email: email.value,
        password: password.value
      })
      const token = response.data.token
      localStorage.setItem('token', token)
      
      window.location.reload()
    } catch (error: any) {
      errorMessage.value = error.response?.data?.message || 'Błąd logowania'
    }
  }
  </script>
  