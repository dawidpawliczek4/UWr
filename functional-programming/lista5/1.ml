
let rec fix f x = f (fix f) x


let fib_f fib n =
  if n <= 1 then n
  else fib (n - 1) + fib (n - 2)

let fib = fix fib_f

let fib10 = fib 10



let rec fix_with_limit i f x = 
  if i = 0 then failwith "ERROR!"
  else
  f (fix_with_limit (i-1) f) x

let fib = fix_with_limit 5 fib_f

let fib10 = fib 10

let htbl = Hashtbl.create 100

let rec fix_memo f x =  
  if Hashtbl.mem htbl x 
  then
    Hashtbl.find htbl x
  else
    let wynik = f (fix_memo f) x in
    Hashtbl.add htbl x wynik; wynik

let fib = fix_memo fib_f