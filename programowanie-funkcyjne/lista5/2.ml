let rec fix f x = f (fix f) x

type 'a self = Self of ('a self -> 'a)
let fix f =
  let g = function Self x -> f (fun v -> x (Self x) v) in
  g (Self g)

let factorial = fix (fun self n -> if n = 0 then 1 else n * self (n - 1))
let _ = print_int (factorial 5)


let fix f =
    let r = ref (fun _ -> failwith "uninitialized") in
    let result x = f (!r) x in
    r := result;
    result