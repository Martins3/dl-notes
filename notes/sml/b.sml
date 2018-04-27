fun map f[] = []
  | map f(x :: xs) = (f x) :: (map f xs);

fun filter f [] =[]
  | filter f (x :: xs) =  if f x then x :: (filter f xs)
                          else filter f xs;

val a = map (fn x=> x + 2);
val b = map(map (fn x=> x + 2));
val c = map(map (fn x=> x + 2))[[1, 2], [3, 4, 5], [6, 7, 8, 9]];
val f = filter (fn a => size a = 4);
val e =  map(filter (fn a => size a = 4));
 val d = map(filter (fn a => size a = 4)) [["hello", "world"],
                                   ["one", "two", "three", "four", "five"],
                                   ["year", "month", "day"]];

