import { Router } from "express";
import { authenticateJWT, authorizeRole } from "../middlewares/authMiddleware";
import Product from "../models/Product";
import User from "../models/User";
import Cart from "../models/Cart";

const router = Router();

// users
router.get(
  "/users",
  authenticateJWT,
  authorizeRole(["admin"]),
  async (req, res) => {
    try {
      const users = await User.find();
      res.json(users);
    } catch (error) {
      res.status(500).json({ message: "Error fetching users", error });
    }
  }
);


// carts
router.get(
  "/carts",
  authenticateJWT,
  authorizeRole(["admin"]),
  async (req, res) => {
    try {
      const cart = await Cart.find();
      res.json(cart);
    } catch (error) {
      res.status(500).json({ message: "Error fetching cart", error });
    }
  }
);


export default router;