const memo = {};
function fib(n) {
  if (n <= 1) return n;
  if (memo[n]) return memo[n];
  memo[n] = fib(n - 1) + fib(n - 2);
  return memo[n];
}

function naiveFib(n) {
  if (n <= 1) return n;
  return naiveFib(n - 1) + naiveFib(n - 2);
}

function memoize(fn) {
  var cache = {};

  return function (n) {
    if (n in cache) {
      return cache[n];
    } else {
      var result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}

naiveFib = memoize(naiveFib)

console.log(naiveFib(1000))