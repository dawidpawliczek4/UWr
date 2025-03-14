type _ fin_type =
  | Unit : unit fin_type
  | Bool : bool fin_type
  | Pair : 'a fin_type * 'b fin_type -> ('a * 'b) fin_type
  | Func : 'a fin_type * 'b fin_type -> ('a -> 'b) fin_type
let seq_to_list (seq : 'a Seq.t) : 'a list =
  let rec aux acc s =
    match s () with
    | Seq.Nil -> List.rev acc
    | Seq.Cons (x, rest) -> aux (x :: acc) rest
  in
  aux [] seq
let rec all_values : type a. a fin_type -> a Seq.t =
  function
  | Bool -> let t = Seq.cons false (Seq.return true) in t
  | Unit -> Seq.return ()
  | Pair (first, second) -> 
    begin
      let fstSeq = all_values first in
      let sndSeq = all_values second in
      Seq.product fstSeq sndSeq
    end
  | Func (x, y) ->
    let arg_values = all_values x in
    let result_values = all_values y in
    let rec generate_functions args =
      match args () with
      | Seq.Nil -> Seq.return (fun _ -> failwith "")
      | Seq.Cons (arg, rest) ->
        let rest_functions = generate_functions rest in
        Seq.flat_map ( fun f ->
          Seq.map ( fun result ->
            ( fun x -> if x = arg then result else f x)
            ) result_values
          ) rest_functions
          in generate_functions arg_values