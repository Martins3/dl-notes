# Divide and conquer
strategy: 
1. divide instance into smaller subinstance
2. solve the subinstance independently 
3. combine solution 

roundabout:
1. 通用的公式是什么

compare dynamic programing:
dp: divide
dc: merge

master method: 

## Example
### merge sort
### closest pair of points
given => set of points P in plane
goal => find min dist(p, p\*)
special case: all in the same line

approach: give a line divide plane to two part
left points : G
right points : R 
line : L

at most one point in each grid
$ = min(dist(G), dist(R))
按照L 为中心的, 左右扩展$的距离, 然后在扩展的区域中间查询是否含有更加小的距离
查询的方法是: 对于y 排序, 然后查询之后的11个 区间

### multiple


### Median / k-th elements
T(n) = T(3/4n) + T(n/5) + O(n) = O(n)


## Network Flow
- finding small cut in graphs
- bipartite graph
- linear programming **???**

questions:  
G = (V, E)  
source sink capacity
a flow is map in (G, c)  f: E -> N  satisfy:
1. capacity 
2. inputs are equal outputs

f_in(v) = sum(f(e)) e = (u, v) belongs to E
f_out(v) = sum(f(e)) e = (v, u) belongs to E

define : value of flow of
|f| = sum(f(s,v)) = sum(f(v, t))

prop: Given any flow f, for any st-cut A, B
(A.contain(a), B.contain(b), A and B is cover of S)
f(A, B) = |f|
其中 f(A, B) = 为A, B 的分割

maximum flow problem:
given flow network (G, c)
find a flow f  maximum value(f)

residual graph
argument path : form s to t , every edge on it has capacity c > 0
bottleneck capacity 

FF Terminal when capacity are integers
value(f) +1 every iteration 而且 value(f) <= output(s)

- WAF(widest Argument Path) => O(m^2log(n) * logV(f*))
- SAP(Shortest Argument Path) => O(m^2 * n)
- Push-relabel maximum flow with dynamic tree
- Push-relabel maximum flow with FIFO vertex selection rule
- Dinitz blocking flow algorithm with dynamic trees

s-t cut in G is a partition A, B of V 
s belongs to A and t belongs to B  
capacity of cut 
flow across(A, B) = (A -> B 总流量) - (B - A 总流量)

let f be a flow in G , the following is equivalent
1. f is a max flow
2. there doesn't exit a path from s to t in Gf

suppose have a flow 
suppose there exist a path, from s to t in Gf
1 -> 2 use the 逆反命题证明  
2 -> 1 : 由于

=> 推论, 最小割的流量就是最大的流


### Network flow 的应用
棒球淘汰赛:   
球队 当前的分数 剩余的场次
解答: 如何创建图,  see the picture 


图像分割:
前景 和 背景 数值为 near 1 和 near 0
分离惩罚值 : 相邻的点分割产生的Wij
需要:
sum(ai) + sum(1- bj) + sum(Wij)

黄金旷工：

