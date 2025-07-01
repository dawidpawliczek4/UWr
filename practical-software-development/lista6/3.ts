// Custom implementation of forEach
function forEach<T>(array: T[], callback: (element: T, index: number, array: T[]) => void): void {
    for (let i = 0; i < array.length; i++) {
        callback(array[i], i, array);
    }
}

// Custom implementation of map
function map<T, U>(array: T[], callback: (element: T, index: number, array: T[]) => U): U[] {
    const result: U[] = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

// Custom implementation of filter
function filter<T>(array: T[], callback: (element: T, index: number, array: T[]) => boolean): T[] {
    const result: T[] = [];
    for (let i = 0; i < array.length; i++) {
        if (callback(array[i], i, array)) {
            result.push(array[i]);
        }
    }
    return result;
}

// Example usage
const numbers = [1, 2, 3, 4, 5];

// forEach example
forEach(numbers, (num, index) => {
    console.log(`Index: ${index}, Value: ${num}`);
});

// map example
const doubled = map(numbers, (num) => num * 2);
console.log('Doubled:', doubled);

// filter example
const even = filter(numbers, (num) => num % 2 === 0);
console.log('Even numbers:', even);
