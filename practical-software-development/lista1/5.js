function fibonacciIterative(n) {
  if (n <= 1) return n;
  let fib = [0, 1];
  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return fib[n];
}

function fibonacciRecursive(n) {
  if (n <= 1) return n;
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}


// for (let i = 0; i < 100; i++) {

// console.log(i + "th Fibonacci number time is: ");

// console.time(fibonacciIterative.name);
// console.log(fibonacciIterative(i));
// console.timeEnd(fibonacciIterative.name);


console.time(fibonacciRecursive.name);
console.log(fibonacciIterative(100_000_000));
console.timeEnd(fibonacciRecursive.name);

// }