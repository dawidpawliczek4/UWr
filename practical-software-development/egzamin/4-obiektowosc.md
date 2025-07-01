### **Notatka do egzaminu – Wykład 4: JavaScript, Obiektowość Prototypowa**

#### **1. Paradygmat obiektowy**
- **Obiekt = stan pamięci + metody do operowania na tej pamięci**
- Języki obiektowe to w zasadzie języki imperatywne z konwencją organizacji kodu wokół obiektów.
- **Klasy, dziedziczenie, konstruktory i operator `new` nie są wymagane**, ale ułatwiają programowanie.
- **Dziedziczenie zapewnia dwie korzyści:**
  1. Oszczędność pamięci (metody współdzielone zamiast kopiowania).
  2. W klasycznych językach – kontrolę typów (w JS brak statycznych typów).
- **Duck Typing** – jeśli obiekt posiada metodę/pole, to można go używać w odpowiednim kontekście.
  ```js
  var person = { name: 'Jan', say: function() { return this.name; } };
  var car = { brand: 'Skoda', say: function() { return this.brand; } };
  function describe(item) { console.log(item.say()); }
  describe(person); // Jan
  describe(car); // Skoda
  ```

---

#### **2. Obiektowość w JS – 3 sposoby tworzenia obiektów**
1. **Literal `{}`**
2. **Funkcja konstruktorowa + `new`**
3. **`Object.create()`**

---

#### **3. Obiektowość z `{ }`, bez dziedziczenia**
- Można tworzyć obiekty bez dziedziczenia, ale każda instancja posiada własne kopie metod:
  ```js
  function Person(name, surname) {
      return { 
          name, surname,
          say: function() { return `${this.name} ${this.surname}`; }
      };
  }
  var p = Person('Jan', 'Kowalski');
  console.log(p.say()); // Jan Kowalski
  ```
- Wadą jest niepotrzebne powielanie metod w każdej instancji.

---

#### **4. Obiektowość prototypowa**
- **Każdy obiekt może mieć prototyp, który zawiera współdzielone metody.**
- **Zmiana prototypu w trakcie działania programu:**
  ```js
  var p = { name: 'Jan', say: function() { return this.name; } };
  var q = {};
  Object.setPrototypeOf(q, p);
  console.log(q.say()); // Jan
  ```
- **Łańcuch prototypów (prototype chain)**
  - Jeśli obiekt nie posiada własnej metody/właściwości, szuka jej w prototypie.
  - `null` oznacza wartość pustą i przerywa poszukiwanie.
  - `undefined` oznacza brak wartości i kontynuuje szukanie w łańcuchu prototypów.
  ```js
  var proto = { foo: 1, bar: 2 };
  var obj = { foo: null };
  Object.setPrototypeOf(obj, proto);
  console.log(obj.foo); // null (bo istnieje w obj)
  console.log(obj.bar); // 2 (bo pochodzi z proto)
  ```
- **Współdzielenie metod poprzez prototypy:**
  ```js
  var personProto = { say: function() { return this.name; } };
  var p1 = { name: 'Jan' };
  Object.setPrototypeOf(p1, personProto);
  var p2 = { name: 'Tomasz' };
  Object.setPrototypeOf(p2, personProto);
  console.log(p1.say()); // Jan
  console.log(p2.say()); // Tomasz
  ```

---

#### **5. Obiektowość z `new`**
- **Funkcja konstruktorowa działa jak klasa w innych językach:**
  ```js
  function Person(name, surname) {
      this.name = name;
      this.surname = surname;
  }
  Person.prototype.say = function() { return `${this.name} ${this.surname}`; };
  var p = new Person('Jan', 'Kowalski');
  console.log(p.say()); // Jan Kowalski
  ```
- **Dziedziczenie w konstruktorach:**
  ```js
  function Worker(name, surname, age) {
      Person.call(this, name, surname);
      this.age = age;
  }
  Worker.prototype = Object.create(Person.prototype);
  Worker.prototype.say = function() {
      return `${Person.prototype.say.call(this)} ${this.age}`;
  };
  var w = new Worker('Jan', 'Kowalski', 48);
  console.log(w.say()); // Jan Kowalski 48
  ```

---

#### **6. Obiektowość przez `Object.create()`**
- **Tworzenie obiektu z określonym prototypem:**
  ```js
  var person = {
      init: function(name, surname) { this.name = name; this.surname = surname; },
      say: function() { return `${this.name} ${this.surname}`; }
  };
  var p = Object.create(person);
  p.init('Jan', 'Kowalski');
  console.log(p.say()); // Jan Kowalski
  ```
- **"Dziedziczenie" przez `Object.create()`:**
  ```js
  var worker = Object.create(person);
  worker.init = function(name, surname, age) {
      person.init.call(this, name, surname);
      this.age = age;
  };
  worker.say = function() {
      return `${person.say.call(this)} ${this.age}`;
  };
  var w = Object.create(worker);
  w.init('Tomasz', 'Malinowski', 48);
  console.log(w.say()); // Tomasz Malinowski 48
  ```

---

#### **7. Równoważność `new` i `Object.create()`**
- `new` można zapisać za pomocą `Object.create()`:
  ```js
  function New(f, ...args) {
      var _ = Object.create(f.prototype);
      var o = f.apply(_, args);
      return o ?? _;
  }
  var p = New(Person, 'Jan', 'Kowalski');
  console.log(p.say()); // Jan Kowalski
  ```
- `Object.create()` można zapisać za pomocą `new`:
  ```js
  function ObjectCreate(proto) {
      function F() {}
      F.prototype = proto;
      return new F();
  }
  var p = ObjectCreate(person);
  p.init('Jan', 'Kowalski');
  console.log(p.say()); // Jan Kowalski
  ```

---

#### **8. Lukier syntaktyczny (`class` i `extends`)**
- **Nowoczesna składnia klas (`ES6+`):**
  ```js
  class Person {
      constructor(name, surname) {
          this.name = name;
          this.surname = surname;
      }
      say() { return `${this.name} ${this.surname}`; }
  }
  class Worker extends Person {
      constructor(name, surname, age) {
          super(name, surname);
          this.age = age;
      }
      say() { return `${super.say()} ${this.age}`; }
  }
  var w = new Worker('Tomasz', 'Malinowski', 48);
  console.log(w.say()); // Tomasz Malinowski 48
  ```
- **Nietypowe zastosowanie `extends` – dziedziczenie z wartości zwracanej przez funkcję:**
  ```js
  function Singleton() {
      return class Singleton {
          static instance;
          static getInstance() {
              if (!this.instance) this.instance = new this();
              return this.instance;
          }
      };
  }
  class Car extends Singleton() {
      paint(color) { this._color = color; }
  }
  let car = Car.getInstance();
  car.paint('red');
  console.log(Car.getInstance()._color); // red
  ```

---

### **Podsumowanie**
- JavaScript używa **obiektowości prototypowej** zamiast klas.
- **Trzy sposoby tworzenia obiektów:** `{}`, `new`, `Object.create()`.
- **Dziedziczenie i współdzielenie metod** jest realizowane poprzez prototypy.
- **`class` to tylko lukier syntaktyczny** nad funkcjami konstruktorowymi i `prototype`.
  
To notatka z kluczowymi koncepcjami wykładu – warto przećwiczyć przykłady! 🚀