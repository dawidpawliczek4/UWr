let build_list n f = 
  let rec aux acc i = 
    if i < 0 then acc
    else aux (f i :: acc) (i-1)
  in
  aux [] (n-1)

let negatives n = build_list n (fun x -> -x)
let list2 = negatives 10

let reciprocals n = build_list n (fun x -> 1.0 /. float_of_int (x+1))
let list3 = reciprocals 10

let evens n = build_list n (fun x -> 2*x)
let list4 = evens 10

let identityMatrix n = build_list n (fun i -> build_list n (fun j -> if i = j then 1 else 0))
let list5 = identityMatrix 4