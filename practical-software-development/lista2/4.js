console.log(typeof 42); // "number"
console.log(typeof 'Hello'); // "string"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof Symbol()); // "symbol"
console.log(typeof {}); // "object"
console.log(typeof []); // "object" (tablice są typu "object")
console.log(typeof function(){}); // "function"

console.log([] instanceof Array); // true
console.log({} instanceof Object); // true
console.log(function(){} instanceof Function); // true
console.log(new Date() instanceof Date); // true
console.log(new Date() instanceof Object); // true (bo wszystkie obiekty dziedziczą z Object)