let suffixes xs =
  let rec sf xs aux =
  match xs with
  | [] -> aux
  | x :: xs' -> sf xs' (xs' :: aux)
  in sf xs [xs]

let lst = [1;2;3]


let suffixes_fold xs =
  List.fold_left (fun acc x ->  List.tl (List.hd acc) :: acc) [xs] xs

let prefixes xs =
  List.fold_left (fun acc x -> (List.hd acc @ [x]) :: acc ) [[]] xs