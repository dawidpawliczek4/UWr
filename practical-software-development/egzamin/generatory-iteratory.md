### **Iteratory i Generatory w JavaScript**
Iteratory i generatory to zaawansowane mechanizmy JavaScript, które pozwalają **leniwe** przetwarzanie danych, dzięki czemu można pracować z potencjalnie nieskończonymi zbiorami lub optymalizować operacje na dużych strukturach danych.

---

## **1. Iteratory**
### **1.1 Co to jest iterator?**
- **Iterator** to obiekt, który implementuje metodę `.next()`, zwracającą kolejny element sekwencji.
- Obiekt ten musi spełniać interfejs:
  ```js
  {
      next: function() {
          return { value: ..., done: ... };
      }
  }
  ```
- **`value`** → aktualna wartość elementu.
- **`done`** → `true`, gdy iteracja się zakończyła.

### **1.2 Tworzenie iteratora "ręcznie"**
```js
function createIterator(array) {
    let index = 0;
    return {
        next: function() {
            if (index < array.length) {
                return { value: array[index++], done: false };
            } else {
                return { done: true };
            }
        }
    };
}

const it = createIterator([1, 2, 3]);
console.log(it.next()); // { value: 1, done: false }
console.log(it.next()); // { value: 2, done: false }
console.log(it.next()); // { value: 3, done: false }
console.log(it.next()); // { done: true }
```

---

## **2. Symbole `Symbol.iterator`**
JavaScript wbudował obsługę iteratorów w wiele struktur, np. `Array`, `Map`, `Set`.

### **2.1 Ręczna implementacja iteratora w obiekcie**
- Aby obiekt był iterowalny (`for...of`, spread `...`), musi mieć metodę `[Symbol.iterator]()`.

```js
const iterableObj = {
    data: [10, 20, 30],
    [Symbol.iterator]: function() {
        let index = 0;
        return {
            next: () => {
                if (index < this.data.length) {
                    return { value: this.data[index++], done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
};

for (let value of iterableObj) {
    console.log(value);
}
// 10
// 20
// 30
```

- **Można używać też z `...spread` i destrukturyzacją**:
  ```js
  console.log([...iterableObj]); // [10, 20, 30]
  ```

---

## **3. Generatory – Funkcje `function*`**
### **3.1 Co to jest generator?**
- **Generator** to funkcja, którą można **wielokrotnie wznawiać**, zamiast wykonywać ją w całości od razu.
- **Zamiast `return` używa `yield`**, który **zatrzymuje funkcję** i zwraca wartość.

```js
function* myGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = myGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { done: true }
```

- **Użycie w `for...of`**:
  ```js
  for (let value of myGenerator()) {
      console.log(value);
  }
  ```

---

### **3.2 Generator jako nieskończony licznik**
```js
function* infiniteCounter() {
    let i = 0;
    while (true) {
        yield i++;
    }
}

const counter = infiniteCounter();
console.log(counter.next().value); // 0
console.log(counter.next().value); // 1
console.log(counter.next().value); // 2
```
- Możemy przerywać iterację w dowolnym momencie.

---

### **3.3 Generator udający `range()` (jak w Pythonie)**
```js
function* range(start, end, step = 1) {
    for (let i = start; i < end; i += step) {
        yield i;
    }
}

for (let num of range(1, 10, 2)) {
    console.log(num);
}
// 1, 3, 5, 7, 9
```

---

## **4. Generatory przyjmujące wartości (`yield` i `.next(value)`)**
- `yield` może też **przyjmować wartości z zewnątrz**.

```js
function* questionGenerator() {
    const name = yield "Jak masz na imię?";
    const age = yield `Cześć ${name}, ile masz lat?`;
    yield `Dziękuję! Masz ${age} lat.`;
}

const gen = questionGenerator();
console.log(gen.next().value); // "Jak masz na imię?"
console.log(gen.next("Jan").value); // "Cześć Jan, ile masz lat?"
console.log(gen.next(25).value); // "Dziękuję! Masz 25 lat."
```

---

## **5. Przerywanie generatorów**
- Możemy **przerwać generator** przez `return()`, zwracając wartość i kończąc działanie.

```js
function* numbers() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = numbers();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.return("Koniec!")); // { value: "Koniec!", done: true }
console.log(gen.next()); // { done: true }
```

---

## **6. Asynchroniczne generatory (`async function*`)**
- **Działają jak standardowe generatory**, ale obsługują `await` i **są asynchroniczne**.

```js
async function* fetchData() {
    const data1 = await fetch("https://jsonplaceholder.typicode.com/posts/1").then(res => res.json());
    yield data1;

    const data2 = await fetch("https://jsonplaceholder.typicode.com/posts/2").then(res => res.json());
    yield data2;
}

(async () => {
    for await (let data of fetchData()) {
        console.log(data);
    }
})();
```

---

## **7. Porównanie iteratorów i generatorów**
| Cecha              | Iterator                     | Generator |
|--------------------|----------------------------|------------|
| Tworzenie         | Ręczne implementowanie `next()` | `function*` |
| Użycie `yield`    | ❌ Nieobsługiwane            | ✅ Obsługiwane |
| Obsługa `return`  | ❌ Brak                      | ✅ Możliwe |
| Asynchroniczność  | ❌ Brak wsparcia             | ✅ `async function*` |
| Wygoda            | ❌ Bardziej skomplikowane     | ✅ Prostota |

---

## **8. Kiedy używać generatorów?**
🔹 **Leniwe przetwarzanie dużych zbiorów danych** (np. duże pliki, streaming).  
🔹 **Iterowanie nieskończonych sekwencji** (np. liczby Fibonacciego).  
🔹 **Efektywne przetwarzanie API (paginacja, lazy-fetch)**.  
🔹 **Zastępowanie skomplikowanych iteratorów**.  

---

## **Podsumowanie**
- **Iteratory** → obiekty z metodą `.next()`, często używane w strukturach danych (`Array`, `Map`, `Set`).
- **Generatory (`function*`)** → ułatwiają tworzenie iteratorów, wspierają `yield`.
- **Asynchroniczne generatory (`async function*`)** → obsługują `await`, świetne do API.
- **Leniwe przetwarzanie danych** to kluczowa zaleta generatorów.

➡ **Warto stosować generatory wszędzie tam, gdzie dane mogą być przetwarzane stopniowo!** 🚀