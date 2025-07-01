
const memo: { [key: number]: number } = {};

function fib(n: number): number {
  if (n <= 1) return n;
  if (memo[n] !== undefined) return memo[n];
  
  memo[n] = fib(n - 1) + fib(n - 2);
  return memo[n];
}

function naiveFib(n: number): number {
  if (n <= 1) return n;
  return naiveFib(n - 1) + naiveFib(n - 2);
}

function memoize(fn: (n: number) => number): (n: number) => number {
  const cache: { [key: number]: number } = {};

  return function (n: number): number {
    if (cache[n] !== undefined) {
      return cache[n];
    } else {
      const result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}

let memoizedNaiveFib = memoize(naiveFib);

console.log(memoizedNaiveFib(1000));
