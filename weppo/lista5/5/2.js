const https = require('https');

// Funkcja zwracająca Promise
function fetchPage(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      let data = '';

      // Odczytywanie danych w częściach
      response.on('data', (chunk) => {
        data += chunk;
      });

      // Zakończenie odczytu
      response.on('end', () => {
        resolve(data); // Zwrócenie danych
      });

      // Obsługa błędów
      response.on('error', (err) => {
        reject(err); // Przekazanie błędu
      });
    }).on('error', (err) => {
      reject(err); // Błąd związany z `https.get`
    });
  });
}

// Użycie funkcji opakowanej w Promise
const url = 'https://jsonplaceholder.typicode.com/posts/1';

fetchPage(url)
  .then((data) => {
    console.log('Zawartość strony:');
    console.log(data);
  })
  .catch((err) => {
    console.error('Wystąpił błąd:', err.message);
  });
