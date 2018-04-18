(*
 *编写函数 interleave: int list * int list -> int list，
 *该函数能实现两个int list数据的合并，且两个list中的元素在结果中交替出现，
 *直至其中一个int list数据结束，
 *而另一个int list数据中的剩余元素则直接附加至结果数据的尾部
 * *)
fun interleave([], []) : int list = []
  | interleave([], R) = R
  | interleave(R, []) = R
  | interleave(a::A, b::B) = [a]@[b]@interleave(A, B);

interleave([2],[4]);
interleave([2,3],[4,5]);
interleave([2,3],[4,5,6,7,8,9]);
interleave([2,3],[ ]);


