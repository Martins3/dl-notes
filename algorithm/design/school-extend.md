
# 贪心算法的证明

## 通用的思路是什么
>”Greedy Exchange” is one of the techniques used in proving the correctness of greedy algorithms.
>The idea of a greedy exchange proof is to incrementally modify a solution produced by any
>other algorithm into the solution produced by your greedy algorithm in a way that doesn’t worsen the
>solution’s quality
[link](http://www.cs.cornell.edu/courses/cs482/2007su/exchange.pdf)
## 具体的实例
1. schedule 问题
假定算法给出的元素为Ａ = {a1, a2 ,...an} , 最优算法为B = {b1, b2, ...,bm}(A,B中间的元素都是
按照时间排序了）, 可以证明 A中第 i个元素的结束的时间不会超过 B中间的第 j个元素的结束的时间,所以
A不可能含有更加少的元素

2. schedule 的最小延迟问题
调换之后, latency 不会增大

3. prim 证明
对于在prim 算法生成的过程中间, A 和 B部分的连接, 必定只有一条边相连接,显然使用prim 提供边不会导致
解变差

4. Kruskal 证明
如果 Kruskal 生成的边的集合为 :　Ｆ, 最优解为　Ｆ\*, 如果　cost(F) > cost(F\*)，必然在Ｆ\*
中间存在一个ｅ 在　Ｆ中间不存在的，同时　F 中间必定存在一个　ｆ 连接　F\* - e (如果不存在那么说明
Ｆ就是不连通的), 所以cost(T∗ − {e}∪{f}) = cost(T∗) −cost(e) +cost(f) ≤ cost(T∗)

## P NP NPC NP-Hard
`Decision Problem`
`Membership Problem`
reducible : 转化
A is black-box reducible to B means: There is a algorithm S, S can invoke B to solve
A

We can take a reductions from A to B as saying A is easier than B
NP -complete means most difficult NP problems

A is in NP, and
for all NP problems B, B is polynomial-time many-one reducible to A.

> 解释, 只要A 可以归约到 B, 表示可以通过B解决的 A, 说明 B 更加难