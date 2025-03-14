### **Notatka do egzaminu – Wykład 5: JavaScript, Modularność, Programowanie Asynchroniczne**

---

## **1. Struktura kodu**
### **1.1 Klasy**
- W innych językach: `class`
- W JavaScript: **funkcje konstruktorowe** lub `class` (lukier syntaktyczny)
  
### **1.2 Składowe prywatne**
- **Naiwne podejście**: domknięcia (problem: większe zużycie pamięci)
  ```js
  function Person(name) {
      var _name = name;
      this.getName = function() { return _name; };
  }
  var p = new Person('Jan');
  console.log(p.getName()); // Jan
  console.log(p._name); // undefined
  ```
- **Lepsze podejście**: `Symbol`
  ```js
  var Person = (function() {
      var nameSymbol = Symbol('name');
      function Person(name) { this[nameSymbol] = name; }
      Person.prototype.getName = function() { return this[nameSymbol]; };
      return Person;
  }());
  var p = new Person('Jan');
  console.log(p.getName()); // Jan
  ```

### **1.3 Przestrzenie nazw (namespaces)**
- JavaScript nie ma `namespace`, ale można użyć obiektów:
  ```js
  var UWr = {};
  UWr.weppo = {};
  UWr.weppo.Person = function(name) { this.name = name; };
  var p = new UWr.weppo.Person('Jan');
  console.log(p.name); // Jan
  ```
- **Poprawne podejście z IIFE** (unikamy redeklaracji):
  ```js
  (function(uwr) {
      uwr.Person = function(name) { this.name = name; };
  })(global.UWr = global.UWr || {});
  ```

### **1.4 Moduły**
- **CommonJS (Node.js)**
  ```js
  // a.js
  module.exports = { work_a };
  let b = require('./b');
  function work_a(n) { if (n > 0) { console.log(`a: ${n}`); b.work_b(n-1); } }
  ```
  ```js
  // b.js
  module.exports = { work_b };
  let a = require('./a');
  function work_b(n) { if (n > 0) { console.log(`b: ${n}`); a.work_a(n-1); } }
  ```
- **ES Modules (`import`/`export`)**
  ```js
  // a.js
  import { b } from './b.js';
  export function a() { console.log('a'); b(); }
  ```
  ```js
  // b.js
  export function b() { console.log('b'); }
  ```
  ```js
  // main.js
  import { a } from './a.js';
  console.log('main');
  a();
  ```
- **Import z aliasem i `export default`**
  ```js
  import b from './b.js';
  export default function a() { console.log('a'); b(); }
  ```
  ```js
  function b() { console.log('b'); }
  export default b;
  ```

### **1.5 Dokumentacja (`JSDoc`)**
- Można generować dokumentację w HTML za pomocą `JSDoc`.

---

## **2. Programowanie asynchroniczne**
### **2.1 Historia**
- Synchroniczne operacje (np. `fopen`, `fread`) blokują procesor.
- **Asynchroniczność** = lepsze wykorzystanie zasobów (zwłaszcza w środowisku wielowątkowym).
- Rozwiązania w różnych językach:
  - C#: `Task`
  - Python: `asyncio.coroutine`
  - JavaScript: **Promise**

### **2.2 Pętla zdarzeń (Event Loop)**
- **Jednowątkowość**: operacje asynchroniczne są kolejkowane do **event loop**.
- **Pseudokod event loop**:
  ```js
  var tasks = [];
  while (tasks.length) {
      let task = tasks.shift();
      task();
  }
  ```
- **Dodanie funkcji do event loop**:
  ```js
  setImmediate(() => { console.log("a"); });
  console.log("b");
  ```
  Wypisze: **b, a** (bo `setImmediate` wykonuje kod po zakończeniu bieżącego zadania).

### **2.3 Callback Hell**
- **Zagnieżdżone wywołania funkcji zwrotnych**:
  ```js
  fs.readFile('1.txt', 'utf-8', function(erra, dataa) {
      fs.readFile('2.txt', 'utf-8', function(errb, datab) {
          fs.readFile('3.txt', 'utf-8', function(errc, datac) {
              console.log(dataa, datab, datac);
          });
      });
  });
  ```
- **Rozwiązanie: wyciąganie funkcji na zewnątrz**:
  ```js
  function readDataC(dataa, datab) {
      fs.readFile('3.txt', 'utf-8', function(errc, datac) {
          console.log(dataa, datab, datac);
      });
  }
  function readDataB(dataa) {
      fs.readFile('2.txt', 'utf-8', function(errb, datab) {
          readDataC(dataa, datab);
      });
  }
  fs.readFile('1.txt', 'utf-8', function(erra, dataa) { readDataB(dataa); });
  ```

### **2.4 Promise**
- **Promise eliminuje Callback Hell**
  ```js
  var p = new Promise((res, rej) => { res(17); });
  p.then(result => console.log(result)); // 17
  ```
- **Promise z operacją asynchroniczną**
  ```js
  var p = new Promise((res, rej) => {
      setTimeout(() => { res(17); }, 1000);
  });
  p.then(result => console.log(result)); // po 1s: 17
  ```
- **Łańcuchowanie `then`**
  ```js
  p.then(result => result + 1)
   .then(result => console.log(result)); // 18
  ```
- **Przekształcanie Callback Hell w Promise**
  ```js
  function fspromise(path, enc) {
      return new Promise((res, rej) => {
          fs.readFile(path, enc, (err, data) => err ? rej(err) : res(data));
      });
  }
  fspromise('a.txt', 'utf-8')
      .then(data => console.log(data))
      .catch(err => console.log(err));
  ```
- **Równoległe wywołania (`Promise.all`)**
  ```js
  Promise.all([
      fs.promises.readFile('1.txt', 'utf-8'),
      fs.promises.readFile('2.txt', 'utf-8')
  ]).then(([data1, data2]) => console.log(data1, data2));
  ```

### **2.5 Async/Await**
- **Łatwiejsza składnia niż `Promise.then()`**
  ```js
  async function main() {
      try {
          let data1 = await fs.promises.readFile('1.txt', 'utf-8');
          let data2 = await fs.promises.readFile('2.txt', 'utf-8');
          console.log(data1, data2);
      } catch (err) {
          console.log(err);
      }
  }
  main();
  ```

### **2.6 Konwersja Callback -> Promise i odwrotnie**
- **`promisify()` (callback -> promise)**:
  ```js
  function promisify(f) {
      return (...args) => new Promise((res, rej) => {
          f(...args, (err, result) => err ? rej(err) : res(result));
      });
  }
  ```
- **`unpromisify()` (promise -> callback)**:
  ```js
  function unpromisify(f) {
      return (...args) => {
          let cb = args.pop();
          f(...args).then(result => cb(null, result)).catch(err => cb(err));
      };
  }
  ```

### **Podsumowanie**
- **Modularność w JS**: CommonJS (`require`), ES Modules (`import/export`).
- **Programowanie asynchroniczne**: Callback Hell → Promise → Async/Await.
- **Zastosowania `Promise.all`**: równoczesne wykonywanie operacji.