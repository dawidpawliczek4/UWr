const https = require('https');

// Adres URL do pobrania zawartości
const url = 'https://jsonplaceholder.typicode.com/posts/1';

// Pobieranie zawartości strony
https.get(url, (response) => {
  let data = '';

  // Odczytywanie danych w częściach
  response.on('data', (chunk) => {
    data += chunk; // Dodawanie kolejnych części danych
  });

  // Po zakończeniu odczytu
  response.on('end', () => {
    console.log('Zawartość strony:');
    console.log(data); // Wyświetlenie danych
  });
}).on('error', (err) => {
  console.error('Wystąpił błąd:', err.message);
});
