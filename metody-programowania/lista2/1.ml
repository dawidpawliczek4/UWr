let rec fibo n =
  if n = 1 then 1
  else if n = 0 then 0
  else fibo (n-1) + fibo (n-2)

let fibo_iter n =
  let rec it a b n =
    if n = 0 then a
    else it b (a+b) (n-1)
  in it 0 1 n