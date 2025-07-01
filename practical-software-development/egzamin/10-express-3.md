### **Notatka do egzaminu – Wykład 10: Express.js (Autoryzacja i Autentykacja)**

---

## **1. Autentykacja i Autoryzacja**
- **Autentykacja** = potwierdzenie tożsamości użytkownika (np. logowanie).
- **Autoryzacja** = przyznanie lub odmowa dostępu do zasobów (np. dostęp do panelu admina).

### **1.1 Metody przechowywania informacji o użytkowniku**
1. **Tylko nazwa użytkownika w ciasteczku**
   - Plus: Uprawnienia mogą się dynamicznie zmieniać.
   - Minus: Konieczność sprawdzania ról przy każdym żądaniu (np. w bazie danych).

2. **Nazwa użytkownika + role w ciasteczku**
   - Plus: Brak potrzeby sprawdzania ról przy każdym żądaniu.
   - Minusy:
     - Zmiana uprawnień wymaga ponownego logowania.
     - Ograniczony rozmiar ciastka.

- **Alternatywa**: zamiast ciastek można użyć `401 Challenge` w HTTP, ale ogranicza on kontrolę nad interfejsem logowania.

---

## **2. Model RBAC (Role-Based Access Control)**
- Każda operacja ma przypisaną rolę użytkownika.
- Przykład:
  - Przeglądanie katalogu – **dla wszystkich**.
  - Składanie zamówienia – **dla zalogowanych użytkowników (User)**.
  - Zarządzanie katalogiem – **tylko dla administratora (Admin)**.

**Problemy RBAC:**
- **Eksplozja zbioru ról** – jeśli użytkownicy mają różne poziomy uprawnień w różnych jednostkach organizacyjnych.
- **Błąd projektowy**: pozwalanie użytkownikowi na tylko **jedną rolę** zamiast wielu.

---

## **3. Middleware do autentykacji (authorize)**
- **Middleware decyduje, czy użytkownik ma dostęp do zasobu**:
  ```js
  function authorize(req, res, next) {
      if (req.signedCookies.user) {
          req.user = req.signedCookies.user;
          next();
      } else {
          res.redirect('/login?returnUrl=' + req.url);
      }
  }
  ```

- **Przykład użycia:**
  ```js
  app.get('/', authorize, (req, res) => {
      res.render('app', { user: req.user });
  });
  ```

- **Obsługa wylogowania:**
  ```js
  app.get('/logout', authorize, (req, res) => {
      res.cookie('user', '', { maxAge: -1 });
      res.redirect('/');
  });
  ```

---

## **4. Strona logowania w Express**
- **Widok `login.ejs`**:
  ```ejs
  <form method="POST">
      <div id='login'>
          <input type='text' name='txtUser' placeholder='Nazwa użytkownika' />
          <input type='password' name='txtPwd' placeholder='Hasło' />
          <button>Zaloguj</button>
          <% if (locals.message) { %>
              <div class='message'><%= locals.message %></div>
          <% } %>
      </div>
  </form>
  ```

- **Obsługa logowania w Express**:
  ```js
  app.post('/login', (req, res) => {
      var username = req.body.txtUser;
      var pwd = req.body.txtPwd;

      if (username == pwd) {
          res.cookie('user', username, { signed: true });
          res.redirect(req.query.returnUrl || '/');
      } else {
          res.render('login', { message: "Zła nazwa logowania lub hasło" });
      }
  });
  ```

---

## **5. Implementacja RBAC w Express**
- **Sprawdzanie ról użytkownika**:
  ```js
  function isUserInRole(user, role) {
      return user == role; // W praktyce lepiej pobierać z bazy
  }
  ```

- **Middleware z kontrolą ról**:
  ```js
  function authorize(...roles) {
      return function (req, res, next) {
          if (req.signedCookies.user) {
              let user = req.signedCookies.user;
              if (roles.length === 0 || roles.some(role => isUserInRole(user, role))) {
                  req.user = user;
                  return next();
              }
          }
          res.redirect('/login?returnUrl=' + req.url);
      };
  }
  ```

- **Przykłady użycia:**
  ```js
  app.get('/', authorize(), (req, res) => res.render('app', { user: req.user }));
  app.get('/admin', authorize('admin'), (req, res) => res.send('Witaj administratorze'));
  ```

---

## **6. Bezpieczeństwo autoryzacji**
### **6.1 Szyfrowane połączenie (SSL/TLS)**
- **Logowanie powinno odbywać się przez HTTPS**.
- **Nie wystarczy szyfrować tylko podczas logowania** – atakujący może przechwycić ciastko w kolejnych żądaniach.

### **6.2 Przechowywanie haseł**
- **Nigdy nie przechowujemy haseł w postaci jawnej**.
- **Zamiast tego stosujemy haszowanie z solą**:
  ```js
  var bcrypt = require('bcrypt');

  (async function() {
      var password = 'Haslo123';
      var rounds = 12;
      var hash = await bcrypt.hash(password, rounds);
      console.log(hash);

      var result = await bcrypt.compare('Haslo123', hash);
      console.log(result); // true
  })();
  ```

- **Bezpieczne haszowanie w bazie**:
  ```
  P = SHA256( … SHA256( SHA256( password + salt ) + salt ) … + salt )
  ```
  - **Używane algorytmy**: `bcrypt`, `PBKDF2`.

---

## **7. Uwierzytelnianie federacyjne (SSO)**
- **Federacyjne logowanie (Single Sign-On, SSO)** = logowanie przez zewnętrznych dostawców (Google, Facebook, etc.).
- **Popularne protokoły SSO**:
  1. **WS-Federation** – stosowany w korporacjach.
  2. **OAuth2 + OpenID Connect** – szeroko stosowany w internecie.

### **7.1 Logowanie przez Google OAuth2**
1. **Rejestracja aplikacji w konsoli Google Developers**.
2. **Konfiguracja OAuth2**:
   ```js
   const oauth2 = new AuthorizationCode({
       client: { id: 'GOOGLE_CLIENT_ID', secret: 'GOOGLE_CLIENT_SECRET' },
       auth: { tokenHost: 'https://www.googleapis.com', authorizeHost: 'https://accounts.google.com' }
   });
   ```

3. **Przekierowanie na stronę logowania Google**:
   ```js
   const authorizationUri = oauth2.authorizeURL({
       redirect_uri: 'http://localhost:3000/callback',
       scope: 'openid profile email'
   });

   app.get('/login', (req, res) => {
       res.render('login', { google: authorizationUri });
   });
   ```

4. **Obsługa odpowiedzi Google (token)**:
   ```js
   app.get('/callback', async (req, res) => {
       const code = req.query.code;
       const result = await oauth2.getToken({ code, redirect_uri: 'http://localhost:3000/callback' });

       const id_token = result.token.id_token;
       const profile = jwt.decode(id_token);

       if (profile.email) {
           res.cookie('user', profile.email, { signed: true });
           res.redirect('/');
       }
   });
   ```

---

## **Podsumowanie**
- **Autoryzacja vs autentykacja** – logowanie ≠ dostęp do zasobów.
- **Model RBAC** – przyznawanie ról użytkownikom.
- **Bezpieczne haszowanie** (`bcrypt`, `PBKDF2`).
- **OAuth2** – uwierzytelnianie przez Google.
- **Middleware autoryzacji** – ochrona ścieżek wymagających logowania.

Następny temat: **Bazy danych w Express.js!** 🚀