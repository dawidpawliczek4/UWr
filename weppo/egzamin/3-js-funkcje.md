### **Notatka do egzaminu – Wykład 3: JavaScript, Funkcje**

#### **1. Funkcje jako obiekty pierwszoklasowe**
- JavaScript traktuje funkcje jako obiekty pierwszoklasowe, co pozwala na:
  - Przekazywanie funkcji jako argumentów do innych funkcji.
  - Zwracanie funkcji jako wartości.
  - Tworzenie funkcji anonimowych.

---

#### **2. Przekazywanie argumentów do funkcji**
- Można wywołać funkcję z dowolną liczbą argumentów, niezależnie od liczby parametrów.
- **Domyślne wartości argumentów:**
  ```js
  function defaultArgs(a=1, b=2) {
      console.log(a, b);
  }
  defaultArgs(); // 1, 2
  ```
- **Pominięcie argumentów:**
  ```js
  function omittedArgs(a, b, c, d, e) {
      console.log(a, b, c, d, e);
  }
  omittedArgs(...[,,],1,...[,,]); // undefined, undefined, 1, undefined, undefined
  ```
- **Zmienna liczba argumentów (arguments, rest operator `...`):**
  ```js
  function overload(a, b) {
      if (arguments.length == 1 && typeof a == 'number') console.log(`overload(int: ${a})`);
      else if (arguments.length == 2 && typeof a == 'string' && typeof b == 'string') 
          console.log(`overload(string: ${a}, string: ${b})`);
      else console.log('nierozpoznane wywołanie');
  }
  overload(1); // overload(int: 1)
  overload('a', 'b'); // overload(string: a, string: b)
  ```

---

#### **3. Zmienne lokalne**
- **Hoisting:** Deklaracje `var` są podnoszone (hoistowane) na początek funkcji, ale nie wartości.
- **Zasięg zmiennych:**
  - `var` – funkcjonalny (widoczny w całej funkcji).
  - `let`, `const` – blokowy (widoczny tylko w danym bloku `{}`).

---

#### **4. Funkcje wyższego rzędu i domknięcia**
- **Funkcje zwracające funkcje i przekazujące je jako argumenty:**
  ```js
  function apply(f, n) { return f(n); }
  console.log(apply(x => x + 1, 1)); // 2
  ```
- **Domknięcia (closures)** – funkcja zapamiętuje swoje środowisko:
  ```js
  function sumpartial(x) {
      return function(y) { return x + y; };
  }
  var sum1 = sumpartial(1);
  console.log(sum1(2)); // 3
  ```

---

#### **5. Przykłady zastosowania domknięć**
- **Funkcja "nieskończona" (łańcuchowe wywołania):**
  ```js
  function sump(x) {
      var _sum = x;
      var _f = function(y) {
          _sum += y;
          return _f;
      };
      _f.valueOf = function() { return _sum; };
      return _f;
  }
  console.log(+sump(4)(5)(6)); // 15
  ```
- **Funkcja samomodyfikująca się:**
  ```js
  function f(s) {
      if (s == "bar") {
          f = function(s) { return s + " zmienione"; };
      }
      return s + " przed zmianą";
  }
  console.log(f('foo')); // foo przed zmianą
  console.log(f('bar')); // bar przed zmianą
  console.log(f('qux')); // qux zmienione
  ```
- **Memoizacja (zapamiętywanie wyników funkcji):**
  ```js
  function memoize(fn) {
      var cache = {};
      return function(n) {
          if (n in cache) return cache[n];
          else return cache[n] = fn(n);
      };
  }
  function fac(n) { return n > 0 ? n * fac(n-1) : 1; }
  var memofac = memoize(fac);
  console.log(memofac(6)); // 720
  ```
- **Currying – częściowa aplikacja funkcji:**
  ```js
  function curry(fn) {
      return function rec(fn, i, args) {
          return i < fn.length 
              ? (x) => rec(fn, i+1, [...args, x]) 
              : fn(...args);
      }(fn, 0, []);
  }
  function sum3(x, y, z) { return x + y + z; }
  console.log(curry(sum3)(1)(2)(3)); // 6
  ```

---

#### **6. IIFE (Immediately-Invoked Function Expression)**
- Funkcja anonimowa, która wywołuje się natychmiast po zadeklarowaniu.
  ```js
  var counter = (function() {
      var i = 0;
      return {
          get: function() { return i; },
          increment: function() { return ++i; }
      };
  })();
  console.log(counter.get()); // 0
  counter.increment();
  console.log(counter.get()); // 1
  ```

---

#### **7. `this`, call, apply, bind**
- **Kontekst `this` zależy od sposobu wywołania:**
  ```js
  function foo() { return this.x; }
  console.log(foo()); // undefined (w strict mode), globalny obiekt w non-strict
  ```
- **Zastosowanie `call`, `apply`, `bind`:**
  ```js
  function foo(y, z) { return this.x + y + z; }
  var obj = { x: 1 };
  console.log(foo.call(obj, 2, 3)); // 6
  console.log(foo.apply(obj, [2, 3])); // 6
  var boundFoo = foo.bind(obj);
  console.log(boundFoo(2, 3)); // 6
  ```

---

#### **8. Iteratory i generatory**
- **Iteratory:**
  ```js
  function createIterator() {
      var state = 0;
      return {
          next: function() {
              return { value: state, done: state++ >= 10 };
          }
      };
  }
  var it = createIterator();
  console.log(it.next().value); // 0
  ```
- **Generatory (skrócona wersja iteratorów):**
  ```js
  function* createGenerator() {
      for (let i = 0; i < 10; i++) yield i;
  }
  var gen = createGenerator();
  console.log(gen.next().value); // 0
  ```
- **Iterowanie po obiekcie za pomocą generatora:**
  ```js
  var obj = { [Symbol.iterator]: createGenerator };
  for (let val of obj) console.log(val);
  ```

---

### **Podsumowanie**
- JavaScript obsługuje **programowanie funkcyjne**, w tym domknięcia, funkcje wyższego rzędu i częściową aplikację.
- **`this` zależy od kontekstu wywołania**, można go wymuszać za pomocą `call`, `apply`, `bind`.
- **Iteratory i generatory** pozwalają na leniwe przetwarzanie danych.
- **IIFE i hoisting** pomagają w organizacji kodu.

To notatka obejmująca kluczowe koncepcje wykładu – warto przećwiczyć przykłady! 🚀