const readline = require('readline');

// Tworzymy interfejs do wprowadzania danych
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Losowanie liczby z zakresu 0–100
const randomNumber = Math.floor(Math.random() * 101);

console.log('Zgadnij liczbę z przedziału od 0 do 100.');

const askQuestion = () => {
  rl.question('Podaj swoją liczbę: ', (input) => {
    const userNumber = parseInt(input, 10);

    // Sprawdzamy, czy podano liczbę
    if (isNaN(userNumber)) {
      console.log('To nie jest liczba! Spróbuj ponownie.');
      return askQuestion();
    }

    // Porównanie wprowadzonej liczby z wylosowaną
    if (userNumber === randomNumber) {
      console.log('To jest właśnie ta liczba! Gratulacje!');
      rl.close(); // Kończymy grę
    } else if (userNumber < randomNumber) {
      console.log('Moja liczba jest większa.');
      askQuestion(); // Pytamy ponownie
    } else {
      console.log('Moja liczba jest mniejsza.');
      askQuestion(); // Pytamy ponownie
    }
  });
};

// Rozpoczęcie gry
askQuestion();
