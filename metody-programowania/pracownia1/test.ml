let build_row ps n =
  (* Funkcja pomocnicza do dodawania pustych miejsc na końcach list. *)
  let add_spaces block = if block = [] then [] else false :: block in

  (* Funkcja rekurencyjna budująca wszystkie kombinacje dla danej listy wskazówek. *)
  let rec build ps remaining_space =
    match ps with
    | [] -> [List.init remaining_space (fun _ -> false)]
    | p :: ps_tail ->
      if p > remaining_space then [] (* Niemożliwe do zbudowania *)
      else
        (* Generuj blok zgodnie z aktualną wskazówką i oblicz pozostałe miejsce. *)
        let block = (List.init p (fun _ -> true)) in
        let new_space = remaining_space - p in
        (* Buduj resztę wiersza rekurencyjnie. *)
        List.concat_map (fun tail ->
          let block_with_space = add_spaces block in
          List.map (fun row -> block_with_space @ row) (build ps_tail (new_space - List.length block_with_space))
        ) [1;0] (* Hack, aby dodać co najmniej jedno puste miejsce między blokami, oprócz ostatniego bloku. *)
  in List.concat_map (fun row -> if List.length row = n then [row] else []) (build ps n)
