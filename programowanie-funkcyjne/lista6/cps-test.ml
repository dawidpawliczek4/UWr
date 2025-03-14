let add x y = x + y
;;
let add_cps x y k = k (x + y)
;;
add_cps 2 3 (fun result -> Printf.printf "Wynik: %d\n" result)


let rec factorial n =
  if n = 0 then 1
  else n * factorial (n - 1)
;;

let rec factorial_cps n k =
  if n = 0 then k 1
  else factorial_cps (n - 1) (fun result -> k (n * result))
;;

factorial_cps 5 (fun result -> Printf.printf "5! = %d\n" result)
;;


let double_cps x k = k (2 * x);;
let increment_cps x k = k (x + 1);;
let composed_cps x k =
  double_cps x (fun doubled ->
    increment_cps doubled (fun incremented ->
      k incremented))
;;
composed_cps 3 (fun result -> Printf.printf "Wynik: %d\n" result)



