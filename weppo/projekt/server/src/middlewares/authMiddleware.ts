import { Request, Response, NextFunction, RequestHandler } from 'express';
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret';


export const authenticateJWT: RequestHandler = (req, res, next) => {
  const authHeader = req.headers['authorization'];

  if (!authHeader) {
    // Even though we’re sending a response here, the function type is still "void".
    // We should just `return` so the function stops executing after sending a response.
     res.status(401).json({ message: 'Missing Authorization header' });
     return
  }

  const token = authHeader.split(' ')[1];
  if (!token) {
     res.status(403).json({ message: 'No token provided' });
     return
  }

  try {
    // Verify token
    const secretKey = JWT_SECRET
    const decoded = jwt.verify(token, secretKey);

    // Attach decoded token to `req.user` if you like
    (req as any).user = decoded; 
    next(); // Continue to the next middleware
  } catch (error) {
    res.status(403).json({ message: 'Failed to authenticate token' });
  }
};

// Middleware do autoryzacji roli
export const authorizeRole = (roles: string[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as any).user;
    if (user.role === "admin") {
      next()
      return
    }
    if (!user || !roles.includes(user.role)) {
      res.status(403).json({ message: 'Forbidden' });
      return
    }
    next();
  };
};
