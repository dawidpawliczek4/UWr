function fibonacciIterator() {
  let a = 0,
    b = 1;
  return {
    next: function () {
      let current = a;
      a = b;
      b = current + b;
      return { value: current, done: false };
    },
  };
}

function* fibonacciGenerator() {
  let a = 0,
    b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

function* take(it, top) {
    let count = 0;
    for (let value of it) {
      if (count++ >= top) return;
      yield value;
    }
  }
  
for (let num of take(fibonacciGenerator(), 10)) {
    console.log(num); // Wypisuje pierwsze 10 liczb Fibonacciego
  }