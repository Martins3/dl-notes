fun is_odd (0 : int) : bool = false
  | is_odd 1 = true
  | is_odd n = is_odd (n - 2);

fun findOdd([]:(int list)): int option = NONE
  | findOdd(x::L) =
  case is_odd(x) of
       true => SOME(x)
     |false => findOdd(L);

val a = [2, 2, 2, 1, 4, 8];
findOdd(a);
findOdd([]);
