(*
 * 编写函数binarySearch: tree * int -> bool
 * 当输出参数1为有序树时，如果树中包含值为参数2的节点，则返回true
 * 否则返回false
 **)

use "./c.sml";
fun binary_search(Lf, _) = false
  | binary_search(Node(L, a, R), x) =
    case Int.compare(x , a) of
      EQUAL => true
    | LESS => binary_search(L, x)
    | GREATER => binary_search(R, x);

val t = Node(Node(Lf, 1, Lf), 2 , Node(Lf, 3, Lf));
binary_search(t, 1);
binary_search(t, 2);
binary_search(t, 3);
