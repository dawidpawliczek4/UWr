(* zad 3 *)

type 'a symbol =
  | T of string
  | N of 'a

type 'a grammar = ('a * ('a symbol list) list) list

let pol : string grammar =
  [ "zdanie", [[N "grupa-podmiotu"; N "grupa-orzeczenia"]]
  ; "grupa-podmiotu", [[N "przydawka"; N "podmiot"]]
  ; "grupa-orzeczenia", [[N "orzeczenie"; N "dopelnienie"]]
  ; "przydawka", [[T "Piękny "];
                  [T "Bogaty "];
                  [T "Wesoły "]]
  ; "podmiot", [[T "policjant "];
                [T "student "];
                [T "piekarz "]]
  ; "orzeczenie", [[T "zjadł "];
                   [T "pokochał "];
                   [T "zobaczył "]]
  ; "dopelnienie", [[T "zupę."];
                    [T "studentkę."];
                    [T "sam siebie."];
                    [T "instytut informatyki."]]]

let expr : unit grammar =
  [(), [[N (); T "+"; N ()];
        [N (); T "*"; N ()];
        [T "("; N (); T ")"];
        [T "1"];
        [T "2"]]]

(*
Random.int : int -> int — losowa liczba z zakresu 0..n-1
List.length : 'a list -> int — długosc listy
List.assoc : 'a -> ('a * 'b ) list -> 'b — wyszukanie elementu na liście asocjacyjnej
String.concat : string -> string list -> string — konkatenacja listy stringów z separatorem
*)

let position x some_list =
  let rec iter i x = function
    | [] -> failwith "Not enough data"
    | head :: tail -> 
      if i = x then head
      else iter (i+1) x tail
  in iter 0 x some_list

let generate g s =
  let rec iter = function
    | T terminal -> terminal
    | N production ->
      let options = List.assoc production g in
      position (Random.int (List.length options)) options
      |> List.map iter
      |> String.concat ""
  in iter (N s)



(* zad 4 *)

(* parens_ok : string -> bool *)
let parens_ok str = 
  let char_list = List.of_seq (String.to_seq str) in
  let rec check stack = function
    | [] -> if stack = [] then true else false
    | head :: tail ->
      if head = '(' then check ( '(' :: stack ) tail
      else if head = ')' then 
        begin
        if stack = [] then false
        else check (List.tl stack) tail
        end
      else failwith "Invalid value"
  in check [] char_list

(* zad 5 *)

let rec check_last = function
  | [] -> failwith "Error"
  | [v] -> v
  | head :: tail -> check_last tail

let rec without_last = function
  | [] -> []
  | [x] -> []
  | head :: tail -> head :: (without_last tail)

let parens_ok_ext str =
  let char_list = List.of_seq (String.to_seq str) in 
  let rec check stack = function
    | [] -> if stack = [] then true else false
    | head :: tail ->
      if head = '(' || head = '[' || head = '{'
        then check (stack @ [head]) tail
      else if head = ')' then         
        begin
        if stack = [] then false
        else if (check_last stack) = '(' then check (without_last stack) tail
        else false        
        end
      else if head = ']' then    
        begin     
        if stack = [] then false
        else if (check_last stack) = '[' then check (without_last stack) tail
        else false        
        end
      else if head = '}' then         
        begin
        if stack = [] then false
        else if (check_last stack) = '{' then check (without_last stack) tail
        else false        
        end
      else failwith "Invalid value"
  in check [] char_list