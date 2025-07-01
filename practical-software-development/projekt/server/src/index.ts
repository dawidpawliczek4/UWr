import express, { Request, Response } from "express";
import productRoutes from "./routes/product";
import authRoutes from "./routes/auth";
import adminRoutes from "./routes/admin";
import cartRoutes from "./routes/cart"
const mongoose = require("mongoose");
require("dotenv").config();
var cors = require('cors')

const app = express();
const port = 3000;
app.use(cors());
app.use(express.json());

app.use("/api/products", productRoutes);
app.use("/api/cart", cartRoutes)
app.use("/auth", authRoutes);
app.use("/admin", adminRoutes);

// Uruchomienie serwera
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

// Funkcja do nawiązania połączenia z MongoDB
const connectDB = async (): Promise<void> => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      // Opcje połączenia (opcjonalnie)
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error("Error connecting to MongoDB:", error);
    process.exit(1); // Zakończ aplikację, jeśli nie można się połączyć
  }
};

// Wywołaj funkcję połączenia
connectDB();
