function isDivisibleByDigitsAndSum(num) {
    const digits = num.toString().split('').map(Number);
    const sumOfDigits = digits.reduce((acc, digit) => acc + digit, 0);
    
    for (let digit of digits) {
        if (digit === 0 || num % digit !== 0) {
            return false;
        }
    }

    if (num % sumOfDigits !== 0) {
        return false;
    }

    return true;
}

function findDivisibleNumbers() {
    const result = [];
    for (let i = 1; i <= 100000; i++) {
        if (isDivisibleByDigitsAndSum(i)) {
            result.push(i);
        }
    }
    return result;
}

const divisibleNumbers = findDivisibleNumbers();
console.log(divisibleNumbers);