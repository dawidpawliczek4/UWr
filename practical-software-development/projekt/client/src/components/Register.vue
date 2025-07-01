<template>
    <div>
      <h1>Rejestracja</h1>
      <form @submit.prevent="handleRegister">
        <div>
          <label for="name">Imię:</label>
          <input id="name" type="text" v-model="name" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input id="email" type="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Hasło:</label>
          <input id="password" type="password" v-model="password" required />
        </div>
        <button type="submit">Zarejestruj</button>
      </form>
      <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
      <p v-if="successMessage" style="color: green">{{ successMessage }}</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import axios from 'axios'
  
  const name = ref('')
  const email = ref('')
  const password = ref('')
  const errorMessage = ref('')
  const successMessage = ref('')
  
  const handleRegister = async () => {
    try {
      const response = await axios.post('http://localhost:3000/auth/register', {
        name: name.value,
        email: email.value,
        password: password.value,
        role: 'user'
      })
      successMessage.value = response.data.message
      errorMessage.value = ''
    } catch (error: any) {
      errorMessage.value = error.response?.data?.message || 'Błąd rejestracji'
      successMessage.value = ''
    }
  }
  </script>
  