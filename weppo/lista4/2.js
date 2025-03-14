function isOwn(obj, propertyName) {
    return obj.hasOwnProperty(propertyName);
}

var p = { name: 'jan' };
var q = { surname: 'kowalski' };

Object.setPrototypeOf(p, q);


console.log(isOwn(p, 'name'));
console.log(isOwn(p, 'surname'));

function listOwnProperties(obj) {
    return Object.keys(obj);
}

console.log(listOwnProperties(p));  // ['name']

function listAllProperties(obj) {
    let properties = [];
    for (let prop in obj) {
        properties.push(prop);
    }
    return properties;
}

console.log(listAllProperties(p));  // ['name', 'surname']