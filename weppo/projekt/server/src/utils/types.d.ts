import { Request } from 'express';

interface UserPayload {
  id: string; // lub `number` jeśli ID użytkownika to liczba
  role: string; // np. 'admin' lub 'user'
  email?: string; // dodatkowe dane
}

// Rozszerzamy typ Request, dodając `user`
export interface AuthenticatedRequest extends Request {
  user: UserPayload;
}
