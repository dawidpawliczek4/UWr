### **Notatka do egzaminu – Wykład 8: Express.js**

---

## **1. Wprowadzenie do Express.js**
- **Express** to **najpopularniejszy framework do aplikacji internetowych w Node.js**.
- Ułatwia **routing, obsługę żądań, sesji, ciasteczek i renderowanie widoków**.
- Wspiera **middleware** – funkcje pośredniczące w obsłudze żądań.
- Alternatywy: **Koa.js, Sails.js**.

**Problemy „naiwnego” podejścia bez frameworka**:
- Duży `if` w funkcji serwera dla różnych ścieżek.
- Brak oddzielenia logiki od HTML-a.
- Ręczne parsowanie parametrów URL i `POST`-a.
- Brak obsługi sesji i ciastek.
- Brak ochrony przed atakami XSS.

---

## **2. Instalacja Express**
```sh
npm install express
```

**Podstawowy serwer Express**:
```js
var express = require('express');
var app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

---

## **3. Middleware – Warstwa kontroli**
- **Middleware** to funkcje obsługujące żądania.
- Każde żądanie przechodzi przez łańcuch middleware’ów.
- Funkcja `next()` przekazuje kontrolę do następnego middleware.

**Przykład middleware w Express:**
```js
var express = require('express');
var app = express();

app.use((req, res, next) => {
    console.log(`Received request for ${req.url}`);
    next();
});

app.get('/', (req, res) => res.send('Hello, World!'));

app.listen(3000);
```

### **Obsługa błędów w Express**
```js
app.use((req, res, next) => {
    if (someCondition) next('Błąd!');
    else res.send('Działa!');
});

app.use((err, req, res, next) => {
    res.status(500).send(`Błąd: ${err}`);
});
```

---

## **4. EJS – Warstwa widoku**
- **EJS (Embedded JavaScript)** to silnik szablonów.
- Pozwala **mieszać kod JS z HTML-em**.
- Używa znaczników:
  - **`<% %>`** – kod JavaScript.
  - **`<%= %>`** – wypisanie wartości.
  - **`<%- %>`** – wypisanie wartości z HTML encodingiem.

**Instalacja:**
```sh
npm install ejs
```

**Konfiguracja Express z EJS:**
```js
var express = require('express');
var app = express();

app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => {
    res.render('index', { username: 'Jan' });
});

app.listen(3000);
```

**Widok `views/index.ejs`:**
```ejs
<!DOCTYPE html>
<html>
<head><title>Express + EJS</title></head>
<body>
    <h1>Witaj, <%= username %>!</h1>
</body>
</html>
```

---

## **5. Dodatkowe elementy architektury aplikacji**
### **5.1 Serwowanie plików statycznych**
- `express.static()` pozwala serwować pliki statyczne.

```js
app.use(express.static('./public'));
```

Plik `public/style.css`:
```css
body { background-color: lightblue; }
```

**Widok `views/index.ejs` z CSS:**
```ejs
<link rel="stylesheet" href="/style.css" />
```

### **5.2 Kontrola nagłówków odpowiedzi**
- Można wymusić pobieranie pliku zamiast jego wyświetlania.

```js
app.get('/download', (req, res) => {
    res.header('Content-disposition', 'attachment; filename="plik.txt"');
    res.send('Zawartość pliku');
});
```

### **5.3 Renderowanie zbiorów danych**
**Widok `views/index.ejs` z listą przelewów:**
```ejs
<table>
    <% przelewy.forEach(przelew => { %>
        <tr>
            <td><%= przelew.data %></td>
            <td><%= przelew.kwota %></td>
            <td><a href="/przelew/<%= przelew.id %>">Więcej</a></td>
        </tr>
    <% }) %>
</table>
```

**Kontroler Express:**
```js
app.get('/', (req, res) => {
    var przelewy = [
        { kwota: 123, data: '2024-02-01', id: 1 },
        { kwota: 124, data: '2024-02-02', id: 2 }
    ];
    res.render('index', { przelewy });
});
```

---

## **6. Obsługa ścieżek dla różnych metod HTTP (GET/POST)**
- **GET** – pobiera dane.
- **POST** – wysyła dane do serwera.

### **Przekazywanie parametrów w URL (`req.query`)**
```js
app.get('/user', (req, res) => {
    var username = req.query.username;
    res.send(`Hello, ${username}`);
});
```
Żądanie:  
```
http://localhost:3000/user?username=Jan
```

### **Obsługa formularzy w Express**
1. Middleware `express.urlencoded()` – do parsowania `POST`:
```js
app.use(express.urlencoded({ extended: true }));
```

2. Formularz `views/index.ejs`:
```ejs
<form method="POST">
    <input type="text" name="username" />
    <button>Zapisz</button>
</form>
```

3. Obsługa formularza w Express:
```js
app.post('/', (req, res) => {
    var username = req.body.username;
    res.redirect(`/userinfo?username=${username}`);
});
```

4. Wyświetlenie przetworzonych danych:
```js
app.get('/userinfo', (req, res) => {
    var username = req.query.username;
    res.render('userinfo', { username });
});
```

**Widok `views/userinfo.ejs`**
```ejs
<h1>Witaj, <%= username %>!</h1>
```

---

## **7. Wzorzec POST-Redirect-GET (PRG)**
- **Unikamy ponownego wysłania formularza przy odświeżeniu strony.**
- **Flow:**
  1. Użytkownik wysyła `POST`.
  2. Serwer przetwarza dane i **przekierowuje** na nowy adres (`GET`).
  3. Przeglądarka wykonuje `GET` i pobiera nowe dane.

**Implementacja PRG w Express:**
```js
app.post('/', (req, res) => {
    var username = req.body.username;
    if (username && username.length > 5) {
        res.redirect(`/userinfo?username=${username}`);
    } else {
        res.render('index', { username, message: 'Min. 6 znaków!' });
    }
});
```

---

## **Podsumowanie**
- **Express.js** ułatwia obsługę HTTP w Node.js.
- **Middleware** pozwala obsługiwać żądania krok po kroku.
- **EJS** pozwala oddzielić kod od HTML-a.
- **Obsługa formularzy i przekierowania (PRG)** zapewnia dobrą UX.
- **Serwowanie plików statycznych** i **renderowanie dynamicznych list**.

Następny temat: **Bazy danych w Express!** 🚀