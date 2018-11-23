fun double x : int = x + x;

fun mapList(f, [])= []
  | mapList(f, x::L)  = f(x)::(mapList(f, L));

val a = [1, 2, 3, 4];
mapList(double, a);
