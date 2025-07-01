type 'a tree = Leaf of 'a | Node of 'a * 'a tree * 'a tree
type 'a ra_list = (int * 'a tree) list

let empty : 'a ra_list = []

(* Funkcja dodająca element na początku listy *)
let rec cons (x : 'a) (xs : 'a ra_list) : 'a ra_list =
  match xs with
  | (w, t1) :: (w', t2) :: ts when w = w' ->
      (1 + w + w', Node (x, t1, t2)) :: ts
  | _ -> (1, Leaf x) :: xs

(* Funkcja zwracająca element na danym indeksie *)
let rec lookup (i : int) (xs : 'a ra_list) =
  match xs with
  | [] -> failwith "Index out of bounds"
  | (w, Leaf x) :: _ when i = 0 -> x
  | (w, Leaf x) :: xs -> lookup (i - 1) xs
  | (w, Node (x, t1, t2)) :: xs ->
      if i = 0 then x
      else if i <= w / 2 then lookup (i - 1) ((w / 2, t1) :: xs)
      else lookup (i - w / 2 - 1) ((w / 2, t2) :: xs)

(* Funkcja usuwająca pierwszy element z listy *)
let rec tail (xs : 'a ra_list) : 'a ra_list =
  match xs with
  | [] -> failwith "Empty list"
  | (1, Leaf _) :: xs -> xs
  | (w, Node (_, t1, t2)) :: xs -> (w / 2, t1) :: (w / 2, t2) :: xs
  | _ -> failwith "Invalid list"