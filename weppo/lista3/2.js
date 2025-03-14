// map
Array.prototype.myMap = function (callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    result.push(callback(this[i], i, this));
  }
  return result;
};
const numbers = [1, 2, 3];
const doubled = numbers.myMap((num) => num * 2);
console.log(doubled);

// forEach
Array.prototype.myForEach = function (callback) {
  for (let i = 0; i < this.length; i++) {
    callback(this[i], i, this);
  }
};
const fruits = ["apple", "banana", "cherry"];
fruits.myForEach((fruit) => console.log(fruit));

//filter
Array.prototype.myFilter = function (callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this)) {
      result.push(this[i]);
    }
  }
  return result;
};
const evenNumbers = numbers.myFilter((num) => num % 2 === 0);
console.log(evenNumbers);
