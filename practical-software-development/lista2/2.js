const obj = [1,2,3].reduce((acc, curr) => {
    acc[curr] = curr
    return acc
}, {})

console.log(obj)

console.log(obj[1])

const test = { a: 'a'}

obj[test] = 'test'

console.log(obj)

const arr = [1,2,'a']
arr['a'] = 'a'

console.log(arr)
console.log(arr[2])