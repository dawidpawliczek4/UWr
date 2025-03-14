### **Notatka do egzaminu – Wykład 6: TypeScript**

---

## **1. Wprowadzenie do TypeScript**
- **TypeScript** to język dodający statyczne typowanie do JavaScript.
- **Każdy kod JavaScript jest poprawnym kodem TypeScript**, ale może powodować błędy kompilacji.
- Typy są opcjonalne – w ich braku stosuje się **inferencję typów**.
- **System typów jest strukturalny** (nie nominalny jak w Java/C#).
- Typy istnieją **tylko w czasie kompilacji** – są usuwane po transpilacji do JavaScript.

---

## **2. Jak używać TypeScript**
### **2.1 TypeScript Playground**
- Interaktywne środowisko do testowania kodu TypeScript.

### **2.2 Instalacja TypeScript (`tsc`)**
- Instalacja globalna:  
  ```sh
  npm install -g typescript
  ```
- Inicjalizacja projektu TypeScript:
  ```sh
  tsc --init
  ```
- Kompilacja plików:
  ```sh
  tsc file.ts
  ```
- Tryb nasłuchiwania zmian:
  ```sh
  tsc --watch
  ```

### **2.3 `ts-node` – uruchamianie TypeScript bez kompilacji**
- Instalacja:
  ```sh
  npm install -g ts-node
  ```
- Uruchamianie kodu TS:
  ```sh
  ts-node file.ts
  ```

### **2.4 Alternatywne środowiska uruchomieniowe**
- **Deno** – nowoczesna alternatywa dla Node.js.
- **Bun** – nowy, szybki runtime.

---

## **3. System typów TypeScript**
### **3.1 Podstawowe informacje**
- **`unknown`** – ogólny typ, nie pozwala na operacje:
  ```ts
  let u: unknown;
  u.foo(); // Błąd
  ```
- **`any`** – pozwala na dowolne operacje (unikać!):
  ```ts
  let a: any;
  a.foo(); // OK
  ```
- **`never`** – typ pusty (np. funkcje, które nigdy nie kończą):
  ```ts
  function fail(): never {
      throw new Error("Błąd");
  }
  ```

### **3.2 Typy literalne**
- **Przypisanie konkretnej wartości jako typ:**
  ```ts
  let _x: 'x' = 'x';
  type X = 'x';
  let _y: X = 'x';
  ```

### **3.3 Inferencja typów**
- TypeScript automatycznie wykrywa typy:
  ```ts
  let a = 1;   // a: number
  let b = true; // b: boolean
  ```

### **3.4 Unie i przecięcia typów**
- **Unia (`|`)** – zmienna może mieć jeden z typów:
  ```ts
  type AorB = 'a' | 'b';
  let a: AorB = 'a'; // OK
  ```
- **Przecięcie (`&`)** – zmienna musi spełniać oba typy:
  ```ts
  type Person = { name: string };
  type Worker = { position: string };
  type Employee = Person & Worker;
  let e: Employee = { name: "Jan", position: "Dev" };
  ```

### **3.5 Type Guards (`typeof`, `in`)**
- **`typeof`** sprawdza typ zmiennej:
  ```ts
  function doWork(p: string | number) {
      if (typeof p === "string") {
          console.log(p.toUpperCase());
      }
  }
  ```
- **`in` sprawdza obecność pola:**
  ```ts
  type Worker = { position: string };
  function isWorker(p: any): p is Worker {
      return "position" in p;
  }
  ```

### **3.6 Przeciążanie funkcji**
- **Kilka deklaracji, jedna implementacja:**
  ```ts
  function sum(a: string, b: string): string;
  function sum(a: number, b: number): number;
  function sum(a: any, b: any) { return a + b; }
  ```

### **3.7 Typy generyczne**
- **Definiowanie funkcji generycznej:**
  ```ts
  function identity<T>(arg: T): T { return arg; }
  let output = identity<string>("hello");
  ```
- **Generyczny filtr:**
  ```ts
  function filter<T>(arr: T[], predicate: (item: T) => boolean): T[] {
      return arr.filter(predicate);
  }
  ```

### **3.8 `keyof`, `typeof`**
- **`keyof` – wyciąganie kluczy jako typów:**
  ```ts
  type Person = { name: string, age: number };
  type Keys = keyof Person; // "name" | "age"
  ```
- **`typeof` – pobieranie typu zmiennej:**
  ```ts
  let settings = { darkMode: true, fontSize: 14 };
  type SettingsType = typeof settings;
  ```

### **3.9 Typy mapowane, warunkowe**
- **Tworzenie nowego typu na podstawie istniejącego:**
  ```ts
  type ReadonlyPerson = { readonly [K in keyof Person]: Person[K] };
  ```
- **Filtrowanie kluczy:**
  ```ts
  type ExcludeKeys<T, U> = T extends U ? never : T;
  type WithoutName = ExcludeKeys<"name" | "age", "name">; // "age"
  ```

### **3.10 Wbudowane typy użytkowe**
- `Partial<T>` – wszystkie pola opcjonalne.
- `Required<T>` – wszystkie pola wymagane.
- `Readonly<T>` – wszystkie pola tylko do odczytu.
- `Pick<T, K>` – wybór tylko określonych pól.
- `Omit<T, K>` – usunięcie określonych pól.

### **3.11 `infer` – wyciąganie typów**
- **Pobieranie typu zwracanego przez funkcję:**
  ```ts
  type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
  type Num = GetReturnType<() => number>; // number
  ```

---

## **4. Klasy w TypeScript**
- **Klasa jako typ i implementacja jednocześnie:**
  ```ts
  class Person {
      constructor(public name: string) {}
      say() { return `Hi, I'm ${this.name}`; }
  }
  ```
- **Implementowanie interfejsu:**
  ```ts
  interface HasName { name: string; }
  class Employee implements HasName {
      constructor(public name: string) {}
  }
  ```

---

## **5. Migracja z JavaScript do TypeScript**
- **Pierwszy krok:** zmiana `.js` → `.ts`, włączenie `allowJs` w `tsconfig.json`.
- **Stopniowe włączanie ścisłych reguł:**
  ```json
  {
    "compilerOptions": {
      "strict": true,
      "noImplicitAny": true,
      "strictNullChecks": true
    }
  }
  ```

---

## **Podsumowanie**
- TypeScript **rozszerza JavaScript o system typów** i inne funkcje.
- Typy są **strukturalne** (nie nominalne).
- Obsługuje **generyczność, mapowanie typów, inferencję i przeciążanie funkcji**.
- Klasy w TS to **implementacja i typ** w jednym.
- TypeScript ułatwia **utrzymanie dużych kodów i migrację z JavaScript**.

To podsumowanie obejmuje kluczowe koncepcje – warto przećwiczyć na przykładach! 🚀