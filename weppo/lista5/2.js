console.log('Podaj swoje imię: ');

process.stdin.on('data', (data) => {
  const name = data.toString().trim(); // Odczyt danych i usunięcie białych znaków
  console.log(`Witaj ${name}!`); // Wyświetlenie powitania
  process.exit(); // Zakończenie programu
});
