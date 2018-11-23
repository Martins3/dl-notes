(*
 *编写函数: treeFilter: (‘a -> bool) -> ‘a tree -> ‘a option tree
 *将树中满足条件P（ ‘a -> bool ）的节点封装成option类型保留，否则替换成NONE
 * *)

datatype 'a tree = Lf | Node of (('a tree) * 'a * ('a tree));

fun treeFilter(f:('a -> bool), Lf) = Lf
  | treeFilter(f, Node(L, x, R)) = case f(x) of
                                     true => Node(treeFilter(f, L),  SOME(x),
                                     treeFilter(f, R))
                                   | false => Node(treeFilter(f, L), NONE,
                                     treeFilter(f, R));

fun is_odd (0 : int) : bool = false
  | is_odd 1 = true
  | is_odd n = is_odd (n - 2);

val a = Node(Lf, 1, Lf);
val b = Node(Lf, 2, Lf);
treeFilter(is_odd, a);
treeFilter(is_odd, b);
