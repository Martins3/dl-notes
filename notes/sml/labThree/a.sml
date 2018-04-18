fun double x : int = x + x;

fun thenAddOne(f: (int -> int), x) = f(x) + 1;

val a = 10;
thenAddOne(double, a);
