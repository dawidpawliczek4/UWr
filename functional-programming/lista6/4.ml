let rec fold_left_cps f_cps acc xs k =
  match xs with
  | [] -> k acc
  | x :: xs' ->
      f_cps acc x (fun acc' ->
        fold_left_cps f_cps acc' xs' k)


let fold_left f acc lst =
  fold_left_cps
    (fun acc x k -> k (f acc x))
    acc lst (fun result -> result)