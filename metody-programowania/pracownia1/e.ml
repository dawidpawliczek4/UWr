let rec build_row spec len =
  let rec prepend n item lst =
    if n <= 0 then lst else prepend (n-1) item (item :: lst) in

  match spec with
  | [] -> [prepend len false []]
  | [x] ->
    List.init (len - x + 1) (fun i ->
      prepend i false [] @ prepend x true [] @ prepend (len - x - i) false [])
  | x :: xs ->
    let rest_with_spaces = prepend 1 false (build_row xs (len - x - 1)) in
    let possible_starts = len - x - List.fold_left (fun acc y -> acc + y + 1) 0 xs in
    List.flatten (
      List.init (possible_starts + 1) (fun i ->
        List.map (fun tail ->
          prepend i false [] @ prepend x true [] @ tail
        ) rest_with_spaces
      )
    )

(* Przykładowe wywołanie funkcji *)
let example_rows = build_row [1; 1] 4;;
