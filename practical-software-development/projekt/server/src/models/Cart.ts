import mongoose, { Schema, Document } from 'mongoose';

export interface ICartItem {
  product: mongoose.Types.ObjectId; // Odniesienie do modelu Product
  quantity: number; // Ilość produktu
}

export interface ICart extends Document {
  user: mongoose.Types.ObjectId; // Odniesienie do modelu User
  items: ICartItem[]; // Lista przedmiotów w koszyku
  totalPrice: number; // Całkowita cena koszyka (opcjonalnie, można obliczać dynamicznie)
}

const CartItemSchema: Schema = new Schema<ICartItem>({
  product: { type: mongoose.Schema.Types.ObjectId, ref: 'Product', required: true },
  quantity: { type: Number, required: true, min: 1 },
});

const CartSchema: Schema = new Schema<ICart>(
  {
    user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true, unique: true }, // Każdy użytkownik ma jeden koszyk
    items: [CartItemSchema], // Lista przedmiotów w koszyku
    totalPrice: { type: Number, default: 0 }, // Opcjonalne pole
  },
  { timestamps: true }
);

const Cart = mongoose.model<ICart>('Cart', CartSchema);

export default Cart;
