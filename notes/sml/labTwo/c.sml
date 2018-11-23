(*
 *编写函数listToTree: int list -> tree
 *将一个表转换成一棵平衡树
 * *)

datatype tree = Lf | Node of tree * int * tree;
val a = Node(Lf , 1 , Lf);


fun split'([]) = ([], [])
  |split'([a]) =([a], [])
  |split'(a::b::L) = let val(M, N) = split'(L) in (a::M, b::M) end;

fun split([]) = ([], 0, [])
  | split([a]) = ([], a, [])
  | split(a::R) = let val (M, N) = split'(R) in  (M, a, N) end;

fun listToTree [] : tree = Lf
  |listToTree R =
  let
    val (L1, x, L2) = split(R)
  in
    Node(listToTree(L1),  x , listToTree(L2))
  end;

val a = [];
val b = [1, 2];
val c = [1, 2, 3];
val d = [1, 2, 3, 4];
val ta = listToTree a;
val tb = listToTree b;
val tc = listToTree c;
val td = listToTree d;
