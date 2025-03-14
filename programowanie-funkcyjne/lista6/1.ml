(* przyjmuje kontynuacje k oczekujaca na napis i akumulator acc, zwraca wynik typu 'a *)
type ('a, 'b) format = (string -> 'b) -> string -> 'a

(* uruchamia format z akumulatorem pustym ("") i przekazuje kontynuacje k *)
let ksprintf (fmt : ('a, 'b) format) (k : string -> 'b) : 'a =
  fmt k ""

(* kontynuacja to funkcja id, ktora konczy rekurencje *)
let sprintf fmt = ksprintf fmt (fun s -> s)

(* przyjmuje staly napis *)
let lit (s: string) (k : string -> 'a) (acc : string) : 'a =
  k (acc ^ s)

(* przyjmuje int *)
let int (k : string -> 'a) (acc : string) (n : int) : 'a =
  k (acc ^ string_of_int n)

(* przyjmuje string *)
let str (k : string -> 'a) (acc : string) (s' : string) : 'a =
  k (acc ^ s')

let ( ^^ ) f g = fun k acc -> f (fun acc' -> g k acc') acc


let ending n =
  if n = 1 then "a"
  else if 1 < n && n < 5 then "y"
  else "ów"

let message =
  sprintf (lit "Ala ma " ^^ int ^^ lit " kot" ^^ str ^^ lit ".")

let result = message 3 (ending 3)

let message = sprintf(lit "Ala ma " ^^ int ^^ lit " kot" ^^ int ^^ lit "." ^^ str ^^ lit ".") 3 2 "a"