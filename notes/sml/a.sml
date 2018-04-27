fun pairself x  = (x, x);

fun drop([], _) = []
  | drop(x::xs, i) = if i > 0 then drop (xs, i - 1)
                     else x::xs;

(fn x=> (x, x)) 4.0;

fun all f[] = true
  |all  f(x::xs) = (f x) andalso all f xs;


