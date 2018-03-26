# Introduction & tilting problem & other examples
[课件的位置](http://www.cs.cornell.edu/courses/cs4820/2014sp)

## tile
如果形状为 I 形状, 使用二分图
如果形状为L, 为hard

<!-- NP and NPC -->

## partition problem
将一个集合分成两个集合, 两个集合数值相等
hard
## Cover the plate
当使用有限的形状骨牌 而且每一个形状的数目无限大的时候, 来填充无穷大平面
undecidable

## interval scheduling
1. 最大的数目最大 : Greedy
2. 每一个任务都是含有value的,要求权重最大: DP(先结束的进行排序, )
## matching
n boys and n girls
matching: set of pairs (g,b), no node is both pair, and the *perfect matching*
indicate that all nodes are include in the set pairs, *stable matching* 
[gale marriage problem](https://en.wikipedia.org/wiki/Stable_marriage_problem)


```
while(there is free boy){
    select a boy m
    m select the favorite girl g
    if(g is free) => (g, b)
    if(g matched m_) => (g, better(m, m_))
}

complexity: O(square(n))
note : result is not unique !
```


## 部分 matching
input: 给出boys and girls, there is only possible matches
a. goal: select max nodes avoid conflict !
b. 如果含有权重, 希望权重最大
c. 必然含有权重, 希望冲突的数目最小


## independent set

证明: independent set  > interval schedule
=> 使用 item request对应, conflict overlap 的对应

证明: independent set > matching
=> 使用 item point之间的连线, conflict point之间的连线含有相同连线

# Greedy
- general design principal
- sequence of decision
    - myopic
    - irrevocable
- analyze
    - greedy steps ahead
    - [exchange method](http://www.cs.cornell.edu/courses/cs482/2003su/handouts/greedy_exchange.pdf)


prove the maximum interval:
    tr : finish time of rth schedule interval
    cr : set of interval in conflict with rth schedule
         compatible with previous schedule 
    1. 所有元素的都是这些集合中间,而且所有的元素不会重复出现
    2.                 

general strategy:
    对于所有的 s -> s1 -> s2 -> s0    

## schedule to minimize latency
    request i, length ti, deadline di
    start time  s = 0
    l = ti + si - di
    SUM(min(max(li))) 
    algorithm: deadline first, start first

## minimal spanning tree
component : if a and b is connected 
tree: undirected connected no circle
forest: undirected no circle
spanning tree: a tree connected all vertex 
MST: minimal weight
lemma : forest G has c connected component with n vertex and m edge,
 then n = m + c

subtract algorithm: find circle and delete the largest edge 
[blue/red edge](http://www.cs.princeton.edu/~wayne/cs423/lectures/mst-4up.pdf): 
define a cut in G
blue rule: find a cut without blue edge, and color the minimum blue
red rule: find a circle c without red edge, colored the maximum weight edge
until all edges all colored and the blue edges

### correctness prove:
empty cut lemma: a graph not connected <==> exited a cut(A, B) without crossing edge
double crossing lemma: for a circle ,if there is a edge e crossing A and B,
then there mush be another edge crossing the edge
lonely cut edge: if e cut(A, B) e doesn't belong cycle

1. feasible : we will get a tree containing all vertex
2. minimal:

prim:
1. 每一步添加构成tree, 图是连通的, 最后依旧为tree
2. 使用贪心证明的通用方法: T* = T - {ek} + {el}, 贪心算法

kruskal

kruskal 的实现: 判断两个点是不是在同一个连通子图中间, 需要使用union find

lemma: for any tree of size n , height h  then n >= pow(2, h) 
归纳法: 对于1 成立
对于两个 treeOne treeTwo 成立, 合并

any sequence of m operations(find and union) take  O(m inverse Ackerman function(m))

path compression:
if edge path are integers, then O(m) Fredman & Wirlend
randomize edge kargar klein tarjan


插叙: 对于满二叉树, 内节点的数目为 n 的时候, 那么leaf 的数目为 n  + 1
1. compare:
    1. greedy: easy to design, hard to prove
    2. dynamic programing: hard and easy

2. dynamic programing:
    1. break down a problem into smaller problems of the same type
    2. large problem depends on small
    3. recursive with remembering or caching

## Sequence alignment / Edit distance
define: first chars {1, 2, 3, 4, 5, 6 ... m}
second chars {1, 2, .... n}
A matching between {1, 2 ... m} and {1, 2, ... n} is an alignment
    if for any (i, j) (i\*, j\*) 属于 M, 那么 i < i\* iff j <  j\*
cost of alignment  sum of all penalties:
opt(i, j) = alignment (x1, xi) == (yi, yj)
opt(m, n) = max(opt(m-1, n-1) + 最后两个字母差距, opt(m -1, n) + 缺失, opt(m, n-1) + 缺失)

可以转化为的: 最短路径的搜索的

变化的问题:
cost:
    i. c(i, j) matching i and j
    ii. c(i) leaving out Xi
    iii. c(j) leaving out Yj

then opt(i, j) = opt(opt(i - 1, j - 1) + c(i, j), opt(i - 1, j) + c(i) , opt(i, j -1) + c(j))

```
init table as follow:
    opt(i, j) = null
    opt(i, 0) = for k  in range(i) sum a_k
    opt(0, j) = .....b_k
    
# 计算的顺序
    for i = max(1, s - m) to min(s, n)
        j = s - i
        compute opt(i ,j) using 递推式
```

## RNA Secondary Structure
给定字符串为 长度为 n
cost(i, j) i j 匹配
cost(i) 跳过自己的成本
找到成本最低的 , 没有跨边的匹配, 允许部分节点没有匹配
opt(1, n) = max(opt(2, n) + cost(1), cost(2, j - 1) + opt(j + 1, n) + cost(i, j))

for length
    for i :
        opt(i, i + length)

复杂度 O(pow(n, 3))

## shortest path with negative/positive edge costs(directed graph with negative cycle)