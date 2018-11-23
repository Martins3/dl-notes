fun is_odd (0 : int) : bool = false
  | is_odd 1 = true
  | is_odd n = is_odd (n - 2);

fun exist(f, []) = false
  | exist(f, a::R) = case f(a) of
                          true => true
                        | false => exist(f, R);

fun forall(f, []) = true
  | forall(f, a::R) = case f(a) of
                          true => forall(f, R)
                        | false => false

val a = [1, 1, 1, 1, 1];
val b = [2, 2, 2, 2, 2];
exist(is_odd, a);
exist(is_odd, b);
forall(is_odd, a);
forall(is_odd, b);

