function createGenerator(max) {
  var _state = 0;
  return {
    next: function () {
      return {
        value: _state,
        done: _state++ >= max,
      };
    },
  };
}

var foo = {
  [Symbol.iterator]: function() {
    return createGenerator(5);
  }
};


for (var f of foo) {
  console.log(f);
}