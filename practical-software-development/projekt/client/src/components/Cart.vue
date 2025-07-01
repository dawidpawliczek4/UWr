<template>
  <div>
    <h1>Koszyk</h1>
    <div v-if="cartItems.length > 0">
      <ul>
        <li v-for="item in cartItems" :key="item.product._id">
          <h3>{{ item.product.name }}</h3>
          <p>Ilość: {{ item.quantity }}</p>
          <p>Cena: {{ item.product.price }} PLN</p>          
          <button @click="removeFromCart(item.product._id)">Usuń</button>
        </li>
      </ul>
      <p><strong>Łączna cena: {{ totalPrice }} PLN</strong></p>
    </div>
    <div v-else>
      <p>Koszyk jest pusty.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

interface IProduct {
  _id: string
  name: string
  description: string
  price: number
  stock: number
}

interface ICartItem {
  product: IProduct
  quantity: number
}

interface ICart {
  items: ICartItem[]
  totalPrice: number
}

const cart = ref<ICart | null>(null)
const cartItems = ref<ICartItem[]>([])

const fetchCart = async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    console.warn('Użytkownik nie jest zalogowany.')
    return
  }
  try {
    const response = await axios.get('http://localhost:3000/api/cart', {
      headers: { Authorization: `Bearer ${token}` }
    })
    cart.value = response.data
    cartItems.value = response.data?.items || []
  } catch (error) {
    console.error('Błąd podczas pobierania koszyka:', error)
  }
}

const removeFromCart = async (productId: string) => {
  const token = localStorage.getItem('token')
  if (!token) {
    console.warn('Użytkownik nie jest zalogowany.')
    return
  }
  try {
    await axios.delete(`http://localhost:3000/api/cart/${productId}`,
    {      
      headers: { Authorization: `Bearer ${token}` }
    })    
    await fetchCart()
  } catch (error) {
    console.error('Błąd podczas usuwania produktu z koszyka:', error)
  }
}

onMounted(() => {
  fetchCart()
})

const totalPrice = computed(() => (cart.value ? cart.value.totalPrice : 0))
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  border-bottom: 1px solid #ccc;
  margin-bottom: 10px;
  padding-bottom: 10px;
}
button {
  margin-top: 10px;
  padding: 6px 12px;
}
</style>
