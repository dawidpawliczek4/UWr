let rec fold_left_cps f_cps acc lst k =
  match lst with
  | [] -> k acc
  | x :: xs ->
      f_cps acc x (fun acc' ->
        fold_left_cps f_cps acc' xs k)


let for_all p xs =
  fold_left_cps
    (fun _ x k ->
      if not (p x) then
        false 
      else
        k true
    )
    true xs (fun result -> result)

let mult_list xs =
  fold_left_cps
    (fun acc x k ->
      if x = 0 then
        0  
      else
        k (acc * x)
    )
    1 xs (fun result -> result)

let sorted xs =
  match xs with
  | [] | [_] -> true  
  | first :: rest ->
      fold_left_cps
        (fun prev x k ->
          if prev > x then
            false  
          else
            k x  
        )
        first rest (fun _ -> true)
