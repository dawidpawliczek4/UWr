const moduleB = require('./moduleB');

module.exports = {
  greet: () => {
    console.log('Hello from module A');
    moduleB.sayHi();
  },
};
