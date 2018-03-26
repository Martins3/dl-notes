# Compute complexity

easy: 
hard: polynomial : graph-coloring   min vertex cut TSP 0-1 knapsack

why difficult:
1. can not find 
2. can not not prove there is a effective way

def: polynomial-time reduction
x <=pY
if we have an method M to solve Y, then we can call Y polynomial times to solve X
(存在Y的解法的, 也就可以解决X)
如果存在多项式的时间解决 Y, 那么存在多项式的时间解决X

example: 
graph coloring: 
1. k kinds of coloring, can you coloring the graph with every neighbors has different
color
2. the minimal kinds of colors to coloring the graph !

传递性: if  X<=pY Y<=pX , then X<=pZ

independent set:
Given a graph G = (V, E)
1. if there is a independent set K 
2. or what is the maximal independent set of G
> independent set means every two vertex didn't connected !

vertex covering: for G = (V, E),
find subset of E every edge has at least one endpoint in the S

the relation with vertex coloring and independent set:
S is vertex covering <=> V/S is a independent set

some definitions :
P NP NPC NP-hard  
P : there is poly-time deterministic algorithm to solve this problem
NP(non deterministic poly-time algorithm)there is two explanation:
1. if find a solution, then can verify in ploy-time
2. if there is a solution, then there is an non-deterministic algorithm to solve it

tree: **what does it wanna say**


P 属于 NP

NPC(NP complete): X 属于 NP, Y 属于 NP, Y<=pX, then X is NP complete

NP hard: 存在 Y 属于 NP, Y<=pX

question: P == NP

if(P = NP) then P=NP=NPC


问题分析:
Cook-Levin: SAT 属于 NPC
boolean variable x1 x2 x3 
clause: (xi V ^xj V xk)
CNF(conjunctive normal form 合取范式: F = ()^()^()



3SAT F = (x1 V ^x2 V x3)
2SAT
可以证明: 3SAT 问题是一个 NPC 问题, 但是2SAT可以多项式的解决

F1 = x1 V x2 V x3 V 4
F2 = (x1 V x2 V D) 与 (x3 V x4 V ^D)

xi 相同赋值情况之下, F1 的可满足性相同

Def Circuit SAT(AND NOT OR)(通过电路图仅仅包含 or not and 连接)
Circuit SAT  属于 NPC
1. Circuit SAT 属于 NP
2. SAT <=pCircuit SAT 

Thm 3SAT 属于 NPC
1. 3SAT 属于 NP
2. SAT <=p 3SAT


SAT: Boolean satisfiability problem

max independent set is NP hard:
3SAT <=p MIS --- A
证明A公式的方法: 对于clause 构成一个三角形, 标记上对应编号, 增加边, 连接
所有x 和 ^x.
那么可以证明, F 可满足 等价于 G 的mis 的大小为clause sentence


1. MIS 属于  NP
2. MIS <=p 3SAT

2SAT 可以使用DP解决:
例子: CNF = (x V y) (x V s) (^x V t) (^x V ｃ)
将xi 和 ^xi 提取出来, 进而消除, 得到之后再次转化为2SAT, 复杂度为 O(n * 3), 
所以2SAT 问题为P问题

3SAT 使用DP
复杂度为O(n ^(2 ^ n))
**为什么数目的总是平方增大**

2SAT 的其他算法:
xi V xj <=> ^xi -> xj V ^xj -> xi 然后构成图, 然后对于的环进行分析.


DPLL(F):
if F is empty, return true
F = UP(F) 单子句传播
F = PureLimitedElimination(F)
F contain empty clause, return False

select a variable X in F by a heuristic
DPLL(x ^ F) true, then 
**see the tutorial**

UP(Unit Propagation): 
**see wiki**

Branching Heuristic:
MOM: 短子句中出现数量最多的
UP: UP最长的(back tracking)
backbone: 最可能被强迫为1 或者 为0 先行解决
**details for the three part !**


simplify the formulate:
regular resolution 
general resolution:
clause learning driving by conflict !
reboot

**what are they**


# 回溯法:
背包问题:
**和背包问题有什么关系**
**分支限界和回溯法有什么关系**

如果接下来搜索不会导致导致更加好的结果, 那么提前停止 !
**八皇后 实现一波**

# 分支限界:
**15格子问题, 如何使用分支限界**
**定理7.1 Less数值是什么**

Max-SAT
eg: x1 x2 ^x1 V x2 
如果有 x1 = x3 = 1 , 2 clause
如果为x1 = x2 = 0 x5 = 1
其他的问题, 
weighted Max-SAT 
partial Max-SAT(hard must, soft max)
weighted partial MAX SAT

eg. 图像Max-cut weight-max-SAT
如果把
**转化的具体的方法是什么**
eg. 最大团(子图, 所有的节点都是的含有联系)

节点: 变元(1 表示在图中间)

节点表示soft clause, 表示为 1
不相邻为的hard clause, 表示不可以同时为1

Brand and Bound for MAX SAT
UP 传播不可以, 求解最大值可以让推导不成立
上界, 当前搜索中间最大值, 没有出现错误子句数目
下界, 估计数值, 没有交集的冲突集()

UP寻找冲突集

SAT and MAX-SAT versus Integer Programing 



 
