function getLastProto(o) {
  var p = o;
  do {
    o = p;
    p = Object.getPrototypeOf(o);    
  } while (p);
  return o;
}


console.log(getLastProto({}))

console.log(getLastProto(function () {}))

console.log(getLastProto(new String()))