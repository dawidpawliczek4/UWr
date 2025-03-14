import { greet } from './moduleA.mjs';

export function sayHi() {
  console.log('Hi from module B');
  greet();
}
