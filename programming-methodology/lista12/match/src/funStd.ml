(* The standard library of FUN *)

let stdlib =
  [ "abs", "fun x -> if x < 0 then 0 - x else x"
  ; "mod", "fun x -> fun y -> x - (x / y) * y"
  ; "fix", "fun f -> (fun x -> fun y -> f (x x) y) 
                     (fun x -> fun y -> f (x x) y)"
  (* zadanie 2 *)
  ; "map", "fun f -> fun lst ->
              match lst with
              | Nil -> Nil
              | Cons(h, t) -> Cons(f h, map f t)"

  ; "append", "fun lst1 -> fun lst2 ->
                  match lst1 with
                  | Nil -> lst2
                  | Cons(h, t) -> Cons(h, append t lst2)"          
  (* zadanie 3 *)
  ; "insert", "fun x -> fun tree ->
    match tree with
    | Empty -> Node(Empty, x, Empty)
    | Node(l, v, r) -> if x < v then Node(insert x l, v, r) else Node(l, v, insert x r)"

  ; "flatten", "fun tree ->
    match tree with
    | Empty -> Nil
    | Node(l, v, r) -> append (flatten l) (Cons(v, flatten r))"

    ; "treesort", "fun lst ->
      let rec build_bst lst tree = 
        match lst with
        | Nil -> tree
        | Cons(h, t) -> build_bst t (insert h tree)
      in flatten (build_bst lst Empty)"
  ]

let parse_string str =
  Parser.prog Lexer.token (Lexing.from_string str)

let include_def (name, str) prog =
  Ast.Let(name, parse_string str, prog)

let include_stdlib prog =
  List.fold_right include_def stdlib prog
