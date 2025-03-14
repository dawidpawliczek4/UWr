### **Notatka do egzaminu – Wykład 9: Express.js (część 2)**

---

## **1. Domyślne middleware do obsługi błędów i XSS**
- Express obsługuje **nieznalezione ścieżki** za pomocą ostatniego `app.use()`:
  ```js
  app.use((req, res, next) => {
      res.render('404.ejs', { url: req.url });
  });
  ```
- **Cross-Site Scripting (XSS)**:
  - Atakujący wstrzykuje kod JavaScript do żądania.
  - Może wykraść dane użytkownika lub przejąć sesję.
  - **Ochrona w EJS:** używanie `<%= %>` zamiast `<%- %>` zapobiega wykonaniu wstrzykniętego kodu.
  - **Błędne podejście (podatność na XSS)**:
    ```ejs
    Strona <%- decodeURIComponent(url) %> nie została znaleziona.
    ```
  - **Poprawne podejście (bezpieczne kodowanie danych użytkownika)**:
    ```ejs
    Strona <%= url %> nie została znaleziona.
    ```

---

## **2. `express-ejs-layouts` – Layouty w Express**
- **Layout** pozwala unikać powielania struktury HTML.
- **Instalacja i użycie:**
  ```sh
  npm install express-ejs-layouts
  ```
  ```js
  var expressLayouts = require('express-ejs-layouts');
  app.use(expressLayouts);
  ```
- **Przykładowy layout `views/layout.ejs`**:
  ```ejs
  <!DOCTYPE html>
  <html>
  <head><title>Express App</title></head>
  <body>
      <%- body %>
  </body>
  </html>
  ```
- **Widok korzystający z layoutu `views/userinfo.ejs`**:
  ```ejs
  Username: <%= username %>
  ```
- **Renderowanie widoku z layoutem:**
  ```js
  app.get('/userinfo', (req, res) => {
      res.render('userinfo', { username: 'Jan', layout: 'layout' });
  });
  ```

---

## **3. Parametry w ścieżkach i atak Web Parameter Tampering**
- **Dynamiczne parametry w ścieżkach**:
  ```js
  app.get('/faktura/:id', (req, res) => {
      res.end(`Faktura nr: ${req.params.id}`);
  });
  ```
  - Adres `http://localhost:3000/faktura/123` zwróci `Faktura nr: 123`.
- **Ograniczenie parametru do liczb (`\d+`)**:
  ```js
  app.get('/faktura/:id(\\d+)', (req, res) => {
      res.end(`Faktura nr: ${req.params.id}`);
  });
  ```
- **Zagrożenie Web Parameter Tampering**:
  - Atakujący modyfikuje adres (`/faktura/999`) i uzyskuje dostęp do cudzych faktur.
  - **Ochrona – dodanie podpisu HMAC do adresu**:
    ```js
    var crypto = require('crypto');
    var secret = 'tajny-klucz';
    var parameter = '1448219';
    var hmac = crypto.createHmac('sha256', secret).update(parameter).digest('hex');
    console.log(hmac);
    ```
    - Bez poprawnego podpisu (`mac=...`) atakujący nie może modyfikować parametru.

---

## **4. Obsługa ciastek (`cookie-parser`)**
- **Middleware do ciastek**:
  ```sh
  npm install cookie-parser
  ```
  ```js
  var cookieParser = require('cookie-parser');
  app.use(cookieParser());
  ```
- **Tworzenie i odczytywanie ciastka**:
  ```js
  app.get('/', (req, res) => {
      let cookieValue = req.cookies.cookie || new Date().toString();
      res.cookie('cookie', cookieValue);
      res.render('index', { cookieValue });
  });
  ```
- **Podpisane ciasteczka (bezpieczniejsze)**:
  ```js
  app.use(cookieParser('tajny-klucz'));
  app.get('/', (req, res) => {
      let cookieValue = req.signedCookies.cookie || new Date().toString();
      res.cookie('cookie', cookieValue, { signed: true });
      res.render('index', { cookieValue });
  });
  ```

---

## **5. Obsługa sesji (`express-session`)**
- **Sesje pozwalają przechowywać stan użytkownika na serwerze zamiast w ciasteczkach.**
- **Instalacja**:
  ```sh
  npm install express-session
  ```
- **Konfiguracja sesji**:
  ```js
  var session = require('express-session');
  app.use(session({ secret: 'tajny-klucz', resave: true, saveUninitialized: true }));
  ```
- **Przykładowe użycie sesji**:
  ```js
  app.get('/', (req, res) => {
      let sessionValue = req.session.sessionValue || new Date().toString();
      req.session.sessionValue = sessionValue;
      res.render('index', { sessionValue });
  });
  ```

---

## **6. Złożone szablony w EJS**
- **Includowanie jednego widoku w drugim**:
  ```ejs
  <%- include('select', { name: 'combo1', options: [ { value: 1, text: 'Opcja 1' } ] }) %>
  ```
- **Widok `views/select.ejs`**:
  ```ejs
  <select name='<%= name %>'>
      <% options.forEach(option => { %>
          <option value='<%= option.value %>'><%= option.text %></option>
      <% }) %>
  </select>
  ```
- **Dynamiczne przekazywanie opcji**:
  ```js
  app.get('/', (req, res) => {
      var combo1 = { name: 'combo1', options: [{ value: 1, text: 'Opcja 1' }] };
      res.render('index', { combo1 });
  });
  ```

---

## **7. Express + TypeScript**
- **Instalacja TypeScript + typów dla Express**:
  ```sh
  npm install -g typescript ts-node
  npm i --save-dev @types/node @types/express
  ```
- **Podstawowy serwer Express w TypeScript (`app.ts`)**:
  ```ts
  import express, { Express, Request, Response } from 'express';

  const app: Express = express();

  app.get('/', (req: Request, res: Response) => {
      res.send('Hello, TypeScript!');
  });

  app.listen(3000, () => console.log('Server started'));
  ```
- **Uruchomienie serwera TypeScript**:
  ```sh
  ts-node app.ts
  ```
- **Rozszerzenie typu `Request` o dodatkowe pole `user`**:
  ```ts
  declare global {
    namespace Express {
      interface Request {
        user: string;
      }
    }
  }
  ```
- **Inny sposób dodania pola do `Request` (bez globalnych modyfikacji)**:
  ```ts
  type RequestWithUser = Request & { user: string };

  app.get('/', (req: Request, res: Response) => {
      const requ = req as RequestWithUser;
      requ.user = 'Jan';
      res.send(`Hello, ${requ.user}!`);
  });
  ```

---

## **Podsumowanie**
- **Middleware** w Express umożliwia obsługę błędów i bezpieczeństwa (XSS).
- **`express-ejs-layouts`** pozwala na reużywalne layouty.
- **Parametry w ścieżkach** mogą prowadzić do ataków `Web Parameter Tampering` – zabezpieczenie przez HMAC.
- **Obsługa ciastek (`cookie-parser`) i sesji (`express-session`)** umożliwia przechowywanie stanu użytkownika.
- **Express + TypeScript** zwiększa bezpieczeństwo i ułatwia pracę dzięki statycznemu typowaniu.

Następny temat: **Bazy danych w Express.js!** 🚀