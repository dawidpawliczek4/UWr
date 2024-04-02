let rec build_row spec len = 
  match spec with
| [] -> [List.init len (fun _ -> false)]
| [x] ->     
    List.init (len - x + 1) (fun i ->
      (List.init i (fun _ -> false)) @ (List.init x (fun _ -> true)) @ (List.init (len - x - i) (fun _ -> false))
    )
| x :: xs ->     
    List.concat_map (fun i ->
      let first_part = (List.init i (fun _ -> false)) @ (List.init x (fun _ -> true)) in
      let rest_len = len - x - i - 1 in
      List.map (fun rest -> first_part @ [false] @ rest) (build_row xs rest_len)
    ) (List.init (len - x - List.length spec + 2) (fun i -> i))

let rec build_row spec len =
  match spec with
  | [] -> [List.init len (fun _ -> false)]  (* Jeśli nie ma specyfikacji, zwróć wiersz pełen `false`. *)
  | [x] ->
      if x > len then []  (* Jeśli specyfikacja nie mieści się w długości, zwróć pustą listę. *)
      else
        List.init (len - x + 1) (fun i ->
          (List.init i (fun _ -> false)) @ (List.init x (fun _ -> true)) @ 
          (List.init (len - x - i) (fun _ -> false))
        )
  | x :: xs ->
      List.concat_map (fun i ->
        let first_part = (List.init (i + 1) (fun _ -> false)) @ (List.init x (fun _ -> true)) in
        let rest_len = len - x - i - 1 in
        if rest_len < 0 then []  (* Zapobiegaj negatywnym długościom. *)
        else
          List.map (fun rest -> first_part @ rest) (build_row xs (rest_len))
      ) (List.init (len - List.fold_left (+) 0 spec - List.length xs) (fun i -> i))
