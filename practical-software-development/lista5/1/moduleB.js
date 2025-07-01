const moduleA = require('./moduleA');

module.exports = {
  sayHi: () => {
    console.log('Hi from module B');
    moduleA.greet();
  },
};
