(*
 * 编写函数reverse和reverse’，要求：
 * 函数类型均为：int list->int list，
 * 功能均为实现输出表参数的逆序输出；
 * 函数reverse不能借助任何帮助函数；
 * 函数reverse’可以借助帮助函数，时间复杂度为O(n)
 * *)
fun reverse [] : int list = []
  | reverse (r::R) = reverse(R)@[r];

fun reverse' x : int list = List.rev x;

val a = [1, 2, 3, 4];
val b = [];
reverse a;
reverse b;

reverse' a;
reverse' b;
