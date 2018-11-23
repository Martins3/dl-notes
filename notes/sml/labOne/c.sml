fun mult[] = 1
  | mult(x::L) = x * (mult L);

fun Mult [] = []
  | Mult (r :: R) = (mult r) :: (Mult R);

val data = [[1, 2, 3], [4, 5, 6]];

Mult data;
