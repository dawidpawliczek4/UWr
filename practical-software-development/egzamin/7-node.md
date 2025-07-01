### **Notatka do egzaminu – Wykład 7: Node.js, HTTP, HTML**

---

## **1. HTTP – Protokół i jego zasada działania**
- **HTTP** to protokół komunikacyjny oparty o **TCP/IP**, zaprojektowany do przekazywania treści multimedialnych.
- W warstwie transportowej HTTP korzysta z **gniazd BSD** (`bind`, `listen`, `accept` na serwerze oraz `connect`, `send`, `recv` na kliencie).
- **Podstawowy problem** w komunikacji opartej o gniazda: **określenie granic komunikacji** (kiedy wysyłać `send`, kiedy oczekiwać `recv`).
- HTTP rozwiązuje to poprzez **konwencję nagłówków i długości treści**.

### **1.1 Struktura żądania HTTP**
- Pierwsza linia żądania określa **typ operacji** (`GET`, `POST`, `PUT`, `DELETE`) oraz zasób (`/index.html`).
- Kolejne linie to **nagłówki HTTP** (np. `Content-Type`, `User-Agent`).
- **Pusta linia** oznacza koniec nagłówków.
- Jeśli żądanie **przesyła dane** (`POST`, `PUT`), wymagany jest nagłówek `Content-Length`.

**Przykład żądania HTTP:**
```
POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

foo=bar&baz=qux
```

### **1.2 Struktura odpowiedzi HTTP**
- Pierwsza linia zawiera kod statusu (`200 OK`, `404 Not Found`).
- Kolejne linie to **nagłówki** (`Content-Type`, `Content-Length`).
- Po pustej linii znajduje się **treść odpowiedzi** (np. HTML, JSON, binaria).

**Przykład odpowiedzi HTTP:**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 27

{"foo": "bar", "baz": "qux"}
```

---

## **2. Narzędzia do analizy ruchu HTTP**
- **Network (Chrome DevTools)** – podgląd ruchu HTTP w przeglądarce.
- **Wireshark** – analiza ruchu sieciowego na niskim poziomie.
- **Fiddler** – HTTP proxy, umożliwia modyfikację żądań i odpowiedzi.
- **Burp Suite** – narzędzie do analizy i testowania aplikacji webowych.

**Przykład wysyłania żądania POST w Node.js:**
```js
var https = require('https');

function promisedRequest() {
    return new Promise((resolve, reject) => {
        var postData = new URLSearchParams({ foo: 'foo', bar: 'bar' }).toString();

        var requestOptions = {
            host: 'httpbin.org',
            port: 443,
            path: '/post',
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': Buffer.byteLength(postData)
            }
        };

        var client = https.request(requestOptions, (res) => {
            var buffer = '';
            res.on('data', (data) => buffer += data.toString());
            res.on('end', () => resolve(buffer));
        });

        client.write(postData);
        client.end();
    });
}

(async function() {
    var result = await promisedRequest();
    console.log(result);
})();
```

---

## **3. Tworzenie serwera HTTP w Node.js**
### **3.1 Podstawowy serwer HTTP**
- Node.js posiada wbudowany moduł `http` do obsługi serwera HTTP.

```js
var http = require('http');

var server = http.createServer((req, res) => {
    res.end(`hello world ${new Date()}`);
});

server.listen(3000);
console.log('Server started on port 3000');
```

- Serwer obsługuje żądania synchronicznie – blokuje wątek, jeśli operacje są czasochłonne.

### **3.2 Serwer HTTP z poprawnym kodowaniem**
```js
var http = require('http');

var server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.end(`hello world ${new Date()}`);
});

server.listen(3000);
console.log('Server started on port 3000');
```

### **3.3 Obsługa żądań GET i POST**
- **Obiekt `req` (`IncomingMessage`)** – przechowuje dane żądania (adres, metoda, nagłówki).
- **Obiekt `res` (`ServerResponse`)** – pozwala na odesłanie odpowiedzi.

```js
var http = require('http');

var server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    if (req.method == 'GET') {
        res.end('<form method="POST"><input name="name"/><button>Send</button></form>');
    } else {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            res.end(`Received: ${body}`);
        });
    }
});

server.listen(3000);
console.log('Server started on port 3000');
```

---

## **4. HTTPS – Bezpieczna wersja HTTP**
### **4.1 Jak działa HTTPS?**
- **Dodaje warstwę szyfrowania SSL/TLS** do HTTP.
- Używa kluczy RSA do **szyfrowania sesji** (klient generuje klucz AES, szyfruje go kluczem publicznym serwera).
- Serwer używa swojego **klucza prywatnego** do odszyfrowania wiadomości.

### **4.2 Tworzenie serwera HTTPS**
```js
var fs = require('fs');
var https = require('https');

(async function () {
    var pfx = await fs.promises.readFile('test.pfx');

    var server = https.createServer({
        pfx: pfx,
        passphrase: 'test'
    }, (req, res) => {
        res.setHeader('Content-Type', 'text/html; charset=utf-8');
        res.end(`hello world ${new Date()}`);
    });

    server.listen(3000);
    console.log('HTTPS server started');
})();
```

---

## **5. HTTP/2**
- **Usprawniona wersja HTTP**, m.in.:
  - **Jedno połączenie TCP** dla wielu zapytań.
  - **Binarny format transmisji** (wydajniejszy niż tekstowy HTTP/1.1).
  - **Multiplexing** – kilka zapytań na raz w jednym strumieniu.
  - **Serwer push** – serwer może wysłać dane przed żądaniem klienta.

**Serwer HTTP/2 w Node.js**
```js
var fs = require('fs');
var http2 = require('http2');

(async function () {
    var pfx = await fs.promises.readFile('test.pfx');

    var server = http2.createSecureServer({
        pfx: pfx,
        passphrase: 'test'
    });

    server.on('stream', (stream, headers) => {
        stream.respond({ 'content-type': 'text/html', ':status': 200 });
        stream.end(`hello world ${new Date()}`);
    });

    server.listen(3000);
    console.log('HTTP/2 server started');
})();
```

---

## **6. Podtrzymanie stanu w HTTP**
- HTTP jest **bezstanowy** – każde żądanie jest niezależne.
- Podtrzymanie stanu wymaga **ciasteczek, sesji lub tokenów**.
- **Przykład sesji w Node.js** (z `querystring` do przetwarzania danych POST):

```js
var qs = require('querystring');

req.on('data', (data) => { postdata += data; });
req.on('end', () => {
    var body = qs.parse(postdata);
    res.end(html.replace('{{name}}', body.login));
});
```

---

## **Podsumowanie**
- **Node.js umożliwia szybkie tworzenie serwerów HTTP/HTTPS**.
- **Asynchroniczność zwiększa wydajność** – zamiast wątków, serwer obsługuje żądania w event loop.
- **HTTP/2 wprowadza optymalizacje** w warstwie transportowej.
- **HTTPS zapewnia bezpieczeństwo** dzięki szyfrowaniu SSL/TLS.

Na kolejnych wykładach: **Express.js** 🚀