fun mapList(f) =
  let
  fun mapList([])= []
    | mapList(x::L)  = f(x)::(mapList(L));
  in
    mapList
  end;

fun double x = x + x;
val kkk = mapList(double);
val data = [1, 2, 3, 4];
kkk(data);

