const fs = require('fs');
const readline = require('readline');

// Ścieżka do pliku z logami
const filePath = 'server.log';

// Tworzenie strumienia odczytu
const fileStream = fs.createReadStream(filePath);

// Tworzenie interfejsu readline
const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
  terminal: false,
});

// Obiekt do przechowywania liczby żądań dla każdego IP
const requestCounts = {};

// Odczyt linii po linii
rl.on('line', (line) => {
  const parts = line.split(' ');
  const ip = parts[1]; // Wyciągamy adres IP

  if (ip) {
    requestCounts[ip] = (requestCounts[ip] || 0) + 1; // Zliczamy żądania
  }
});

// Po zakończeniu odczytu pliku
rl.on('close', () => {
  // Sortowanie adresów IP według liczby żądań malejąco
  const sortedIps = Object.entries(requestCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3); // Pobranie top 3 adresów IP

  console.log('Najczęściej odwiedzające adresy IP:');
  sortedIps.forEach(([ip, count], index) => {
    console.log(`${index + 1}. ${ip} - ${count} żądań`);
  });
});
