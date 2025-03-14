import { sayHi } from './moduleB.mjs';

export function greet() {
  console.log('Hello from module A');
  sayHi();
}
