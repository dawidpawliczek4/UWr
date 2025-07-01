import { Request, Response, Router } from "express";
import { AuthenticatedRequest } from "../utils/types";
import Cart from "../models/Cart";
import Product from "../models/Product"; // Import modelu produktu
import { authenticateJWT, authorizeRole } from "../middlewares/authMiddleware";

const calculateTotalPrice = async (cart: any): Promise<number> => {
  let totalPrice = 0;

  for (const item of cart.items) {
    const product = await Product.findById(item.product);
    if (product) {
      totalPrice += product.price * item.quantity;
    }
  }

  return totalPrice;
};

const router = Router();

router.post("/", authenticateJWT, authorizeRole(["user"]), async (req, res) => {
  const userId = req.user?.id;
  const { productId, quantity } = req.body;

  try {    
    const product = await Product.findById(productId);
    if (!product) {
      res.status(404).json({ message: "Product not found" });
      return;
    }

    let cart = await Cart.findOne({ user: userId });
    if (!cart) {      
      cart = new Cart({ user: userId, items: [] });
    }
    
    const existingItem = cart.items.find(
      (item) => item.product.toString() === productId
    );

    if (existingItem) {      
      existingItem.quantity += quantity;
    } else {      
      cart.items.push({ product: productId, quantity });
    }
    
    cart.totalPrice = await calculateTotalPrice(cart);

    await cart.save();

    res.status(200).json(cart);
  } catch (error) {
    console.error("Error adding to cart:", error);
    res.status(500).json({ message: "Error adding to cart" });
  }
});
router.delete(
  "/:id",
  authenticateJWT,
  authorizeRole(["user"]),
  async (req, res) => {
    const userId = req.user?.id;    
    const productId = req.params.id;
  
    try {
      const cart = await Cart.findOne({ user: userId });
      if (!cart) {
        res.status(404).json({ message: "Cart not found" });
        return;
      }
      
      cart.items = cart.items.filter(
        (item) => item.product.toString() !== productId
      );
  
      cart.totalPrice = await calculateTotalPrice(cart);
  
      await cart.save();
  
      res.status(200).json(cart);
    } catch (error) {
      console.error("Error removing from cart:", error);
      res.status(500).json({ message: "Error removing from cart" });
    }
  }
); 
router.get("/", authenticateJWT, authorizeRole(["user"]), async (req, res) => {
  const userId = req.user?.id;
  try {
    const cart = await Cart.findOne({ user: userId }).populate("items.product");
    if (!cart) {
      res.status(404).json({ message: "Cart not found" });
      return;
    }

    res.status(200).json(cart);
  } catch (error) {
    console.error("Error fetching cart:", error);
    res.status(500).json({ message: "Error fetching cart", error });
  }
});

export default router;


