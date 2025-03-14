let rec sublists xs =
  match xs with
  | [] -> [[]]
  | x :: xs' -> 
    let sub_xs' = sublists xs' in
    (* sub_xs' @ List.map ( fun sl -> x :: sl) sub_xs' *)
    List.fold_left (fun acc sl -> (x :: sl) :: sl :: acc) [] sub_xs'