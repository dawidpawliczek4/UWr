let length xs = List.fold_left (fun acc x -> acc + 1) 0 xs

let example_list = [3;4;5;1;2]

let example_length = length example_list


let rev xs = List.fold_left (fun acc x -> x :: acc) [] xs

let example_rev = rev example_list

let append xs ys = List.fold_right (fun x acc -> x :: acc) xs ys

let example_append = append [1;2;3] [3;4;5]

let rev_append xs ys = List.fold_left (fun acc x -> x :: acc) ys xs

let filter f xs = List.fold_right (fun x acc -> if f x then x :: acc else acc) xs []

let ex_f x = x mod 2 = 0


let rev_map f xs = List.fold_left (fun acc x -> f x :: acc) [] xs
