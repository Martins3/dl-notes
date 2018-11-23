(*
 * 编写函数revT: tree -> tree，对树进行反转，
 * 使trav(revT t) = reverse(trav t)
 * *)
use "./c.sml";
fun reT Lf = Lf
  | reT(Node(L, a, R)) = Node(reT(R), a, reT(L));

reT(ta);
reT(tb);
reT(tc);
reT(td);
