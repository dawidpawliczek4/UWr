<template>
  <div>
    <nav>
      <button @click="currentView = 'products'">Produkty</button>
      <button @click="currentView = 'cart'">Koszyk</button>      
      <button v-if="!isAuthenticated" @click="currentView = 'login'">Login</button>
      <button v-if="!isAuthenticated" @click="currentView = 'register'">Rejestracja</button>      
      <button v-if="isAuthenticated" @click="logout">Wyloguj</button>
    </nav>
    <component :is="currentViewComponent" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import ProductList from './components/ProductList.vue'
import Cart from './components/Cart.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'

const currentView = ref('products')

const isAuthenticated = computed(() => !!localStorage.getItem('token'))

const currentViewComponent = computed(() => {
  switch (currentView.value) {
    case 'products':
      return ProductList
    case 'cart':
      return Cart
    case 'login':
      return Login
    case 'register':
      return Register
    default:
      return ProductList
  }
})

const logout = () => {
  localStorage.removeItem('token')
  currentView.value = 'products'
}
</script>

<style scoped>
nav {
  margin-bottom: 20px;
}
button {
  margin-right: 10px;
  padding: 8px 16px;
  font-size: 16px;
}
</style>
