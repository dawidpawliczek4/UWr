<template>
    <div>
      <h1>Lista Produktów</h1>
      <input
        type="text"
        v-model="search"
        placeholder="Wyszukaj produkty"
        @input="fetchProducts"
      />
      <ul>
        <li v-for="product in products" :key="product._id">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <p>Cena: {{ product.price }} PLN</p>
          <button @click="addToCart(product)">Dodaj do koszyka</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  interface IProduct {
    _id: string
    name: string
    description: string
    price: number
    stock: number
  }
  
  const products = ref<IProduct[]>([])
  const search = ref('')
  
  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://localhost:3000/api/products', {
        params: { search: search.value }
      })
      products.value = response.data
    } catch (error) {
      console.error('Błąd podczas pobierania produktów:', error)
    }
  }
  
  onMounted(() => {
    fetchProducts()
  })
  
  const addToCart = async (product: IProduct) => {    
    const token = localStorage.getItem('token')
    if (!token) {
      alert('Musisz być zalogowany, aby dodać produkt do koszyka.')
      return
    }
    try {
      await axios.post(
        'http://localhost:3000/api/cart',
        { productId: product._id, quantity: 1 },
        {
          headers: { Authorization: `Bearer ${token}` }
        }
      )
      alert('Produkt został dodany do koszyka!')
    } catch (error) {
      console.error('Błąd podczas dodawania do koszyka:', error)
    }
  }
  </script>
  
  <style scoped>
  input {
    padding: 8px;
    width: 300px;
    margin-bottom: 20px;
  }
  li {
    list-style: none;
    margin-bottom: 20px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 10px;
  }
  button {
    margin-top: 10px;
    padding: 6px 12px;
  }
  </style>
  