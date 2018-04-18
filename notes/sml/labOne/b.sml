fun mult[] = 1
  | mult(x::L) = x * (mult L);

(* test *)
val w = [1, 2, 3, 4, 5];
mult w;