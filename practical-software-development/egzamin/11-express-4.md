### **Notatka do egzaminu – Wykład 11: Express.js (SPA, REST, WebSockets, Deployment)**

---

## **1. Single-Page Applications (SPA) i AJAX**
- **SPA (Single Page Application)** – aplikacja internetowa, w której:
  - Po pierwszym załadowaniu strony brak klasycznej nawigacji.
  - Treść zmienia się dynamicznie poprzez manipulacje na DOM.
  - Dane pobierane są asynchronicznie z serwera za pomocą **AJAX**.

### **1.1 AJAX – Asynchronous JavaScript And XML**
- **AJAX** to technika wysyłania żądań do serwera z poziomu JavaScript **bez przeładowania strony**.
- **AHAH (Asynchronous HTML and HTTP)** – serwer zwraca HTML, który jest dynamicznie wstawiany do strony.
- **AJAJ (Asynchronous JavaScript and JSON)** – serwer zwraca dane w formacie JSON, które są przetwarzane przez JS.

### **1.2 Obsługa AJAX w Express**
- **Serwer (`app.js`) obsługujący żądania AJAX:**
  ```js
  var express = require('express');
  var multer = require('multer');
  var app = express();
  var upload = multer();

  app.post('/ajax', upload.single(), (req, res) => {
      var txtParam = req.body.txtParam;
      res.end(`<div>dynamiczna zawartość: ${txtParam}</div>`);
  });

  app.get('/', (req, res) => {
      res.render('app');
  });

  app.listen(3000, () => console.log('Serwer działa'));
  ```

- **Klient (`views/app.ejs`) wysyłający żądanie AJAX:**
  ```ejs
  <script>
    window.addEventListener('load', function() {
        document.getElementById('btApp').addEventListener('click', async function() {
            var param = document.getElementById('txtParam').value;
            var form = new FormData();
            form.append('txtParam', param);

            var response = await fetch('/ajax', { body: form, method: 'post' });
            var responseText = await response.text();
            document.getElementById('content').innerHTML = responseText;
        });
    });
  </script>
  ```

---

## **2. REST API – Representational State Transfer**
- REST to **architektura API**, gdzie:
  - **Różne metody HTTP reprezentują operacje**:
    - `GET` – pobranie danych.
    - `POST` – dodanie nowych danych.
    - `PUT` – aktualizacja danych.
    - `DELETE` – usunięcie danych.
  - **Adresy URL reprezentują zasoby**, np.:
    - `/api/User` – lista użytkowników.
    - `/api/User/1` – dane użytkownika o `id=1`.

### **2.1 Przykładowe REST API w Express**
```js
var express = require('express');
var app = express();
app.use(express.json());

var users = [{ id: 1, name: 'Jan' }, { id: 2, name: 'Anna' }];

app.get('/api/users', (req, res) => res.json(users));
app.get('/api/users/:id', (req, res) => res.json(users.find(u => u.id == req.params.id)));
app.post('/api/users', (req, res) => {
    let user = { id: users.length + 1, name: req.body.name };
    users.push(user);
    res.status(201).json(user);
});
app.put('/api/users/:id', (req, res) => {
    let user = users.find(u => u.id == req.params.id);
    if (user) user.name = req.body.name;
    res.json(user);
});
app.delete('/api/users/:id', (req, res) => {
    users = users.filter(u => u.id != req.params.id);
    res.status(200).end();
});

app.listen(3000, () => console.log('REST API działa'));
```

### **2.2 Dokumentacja API – OpenAPI/Swagger**
- **OpenAPI** to standard opisu API.
- **Swagger** to narzędzie do generowania dokumentacji API.
- **Przykładowy opis OpenAPI (`swagger.json`)**:
  ```json
  {
    "openapi": "3.0.0",
    "info": { "title": "User API", "version": "1.0.0" },
    "paths": {
      "/api/users": {
        "get": { "summary": "Get all users" },
        "post": { "summary": "Add a user" }
      }
    }
  }
  ```

---

## **3. WebSockets – Dwukierunkowa Komunikacja w Czasie Rzeczywistym**
- **WebSockets** umożliwiają **dwukierunkową komunikację** między przeglądarką a serwerem.
- **Serwer odpowiada kodem `101 Switching Protocols`**, zmieniając połączenie HTTP w stałe połączenie WebSocket.

### **3.1 Implementacja WebSocket z `socket.io`**
- **Instalacja `socket.io`**:
  ```sh
  npm install socket.io
  ```
- **Serwer WebSocket (`app.js`)**:
  ```js
  var http = require('http');
  var socket = require('socket.io');
  var express = require('express');
  var app = express();
  var server = http.createServer(app);
  var io = socket(server);

  io.on('connection', (socket) => {
      console.log('Klient podłączony: ' + socket.id);
      socket.on('chat message', (msg) => io.emit('chat message', msg));
  });

  server.listen(3000, () => console.log('WebSocket działa'));
  ```

- **Klient WebSocket (`views/app.ejs`)**:
  ```ejs
  <script src="/socket.io/socket.io.js"></script>
  <script>
    window.addEventListener('load', function() {
        var socket = io();
        document.getElementById('btsend').addEventListener('click', function() {
            var msg = document.getElementById('txtmessage').value;
            socket.emit('chat message', msg);
        });
        socket.on('chat message', function(msg) {
            document.getElementById('messages').innerHTML += msg + "<br/>";
        });
    });
  </script>
  ```

---

## **4. Deployment – Wdrażanie Aplikacji Express**
- **Deployment** = umieszczenie aplikacji w środowisku produkcyjnym.
- **Continuous Deployment (CD)** = automatyczne wdrażanie po każdym zatwierdzeniu zmian w repozytorium.

### **4.1 Hosting Node.js**
- **Dostępne opcje:**
  - **Render** (https://render.com/)
  - **Vercel** (https://vercel.com/)
  - **Cyclic.sh** (https://www.cyclic.sh/)
  - **AWS, Google Cloud, Azure**

### **4.2 Wdrażanie aplikacji na Heroku**
1. **Dodanie skryptu startowego w `package.json`**:
   ```json
   "scripts": { "start": "node app.js" }
   ```
2. **Ignorowanie `node_modules` w `.gitignore`**:
   ```
   node_modules
   ```
3. **Modyfikacja kodu do obsługi portu Heroku**:
   ```js
   app.listen(process.env.PORT || 3000);
   ```
4. **Deploy do Heroku**:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   heroku login
   heroku create
   git push heroku master
   ```

---

## **Podsumowanie**
- **SPA** i **AJAX** pozwalają na dynamiczne odświeżanie treści bez przeładowania strony.
- **REST API** umożliwia komunikację między frontendem a backendem za pomocą metod HTTP.
- **WebSockets (`socket.io`)** zapewniają komunikację w czasie rzeczywistym.
- **Deployment na Heroku, Render, Vercel** ułatwia udostępnianie aplikacji w chmurze.

To podsumowanie obejmuje kluczowe koncepcje – warto przećwiczyć na przykładach! 🚀