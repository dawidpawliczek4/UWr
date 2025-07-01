// const fib = (n: number): number => {
//     if (n <= 1) return n;
//     return fib(n - 1) + fib(n - 2);
// };

// type MemoizeFn<T extends (...args: any[]) => any> = T & {
//     cache: Map<string, ReturnType<T>>;
// };

// function memoize<T extends (...args: any[]) => any>(fn: T): MemoizeFn<T> {
//     const cache = new Map<string, ReturnType<T>>();

//     const memoizedFn: MemoizeFn<T> = ((...args: Parameters<T>) => {
//         const key = JSON.stringify(args);
//         if (cache.has(key)) {
//             return cache.get(key) as ReturnType<T>;
//         }
//         const result = fn(...args);
//         cache.set(key, result);
//         return result;
//     }) as MemoizeFn<T>;

//     memoizedFn.cache = cache;
//     return memoizedFn;
// }

// const memoizedFib = memoize(fib);


// console.log(memoizedFib(10));
// console.log(memoizedFib(15));
// console.log(memoizedFib.cache);
