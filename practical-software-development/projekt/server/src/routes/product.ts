import { Router } from 'express';
import Product from '../models/Product';
import { authenticateJWT, authorizeRole } from '../middlewares/authMiddleware';

const router = Router();

router.get('/', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching products', error });
  }
});

router.delete("/:id", authenticateJWT, authorizeRole(["admin"]), async (req, res) => {
  try {
    const deleted = await Product.findByIdAndDelete(req.params.id)
    if (!deleted) {
      res.status(404).json({ message: "Error deleting product"})
    }
    res.json({ message: "Product has been deleted"})    
  }
  catch (err) {
    res.status(500).json({message: "Server error"})
  }
})

router.put("/:id", authenticateJWT, authorizeRole(["admin"]), async (req, res) => {
  try {
    const updated = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updated) { 
      res.status(404).json({ message: 'Product to update not found' }) 
    }
    res.json(updated);
  } catch (err) {
    res.status(500).json({ message: "Server error" })
  } 
})

router.post("/:id", authenticateJWT, authorizeRole(["admin"]), async (req, res) => {
  const { name, description, price, stock } = req.body;
  try {
    const product = new Product({ name, description, price, stock });
    await product.save();
    res.status(201).json(product);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
})

router.get("/:id", async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) { res.status(404).json({ message: 'Product not found' })}
    res.json(product);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
})

export default router;
