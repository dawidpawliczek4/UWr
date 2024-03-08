let matrix_mult (a1, a2, a3, a4) (b1, b2, b3, b4) = 
  (a1 *. b1 +. a2 *. b3, a1 *. b2 +. a2 *. b4, a3 *. b1 +. a4 *. b3, a3 *. b2 +. a4 *. b4)

let matrix_id = (1., 0., 0., 1.)

let matrix_expt m k = 
  let rec mnozenie m k acc =
    if k = 0 then acc
    else mnozenie m (k-1) (matrix_mult m acc) in
  mnozenie m k matrix_id

let fib_matrix k =
  let rec mnozenie m k acc =
    if k = 0 then acc
    else mnozenie m (k-1) (matrix_mult m acc) in
  let (a, _, _, _) = mnozenie (1., 1., 1., 0.) k matrix_id in
  a


  

let matrix_expt_fast m k = 
  let rec poteguj m k acc =
    if k = 0 then acc
    else if k mod 2 = 0 then poteguj (matrix_mult m m) (k / 2) acc
    else poteguj (matrix_mult m m) (k / 2) (matrix_mult m acc)
  in
  poteguj m k matrix_id

let fib_fast k =
  if k = 0 then 0.
  else
    let (a, b, _, _) = matrix_expt_fast (1., 1., 1., 0.) (k - 1) in
    b