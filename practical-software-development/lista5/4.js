const fs = require('fs').promises;

// Ścieżka do pliku, który chcemy odczytać
const filePath = 'example.txt';

// Odczyt pliku za pomocą obietnic
fs.readFile(filePath, 'utf8')
  .then((data) => {
    console.log('Zawartość pliku:');
    console.log(data);
  })
  .catch((err) => {
    console.error('Wystąpił błąd podczas odczytu pliku:', err.message);
  });
