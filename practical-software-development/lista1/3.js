function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

function findPrimes() {
    const primes = [];
    for (let i = 2; i <= 100000; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}

const primes = findPrimes();
console.log(primes);