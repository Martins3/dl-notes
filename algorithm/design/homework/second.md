#### Homework Two

#### 1 MST 并行算法
##### Boruvka's Algorithm
```
Graph is noted as G, G's vertex set and edge set are noted as V and E
init a forest F containing V, for every vertex is a segment
while F has more than one components:
    for every segment S:
        if e is cheapest edge of S:
            add e to F
```
##### Karger, Klein, and Tarjan's Algorithm 
```
1. Apply two successive Borfivka steps to the graph, thereby reducing
the number of vertices by at least a factor of four.
2. In the contracted graph, choose a subgraph H by selecting each
edge independently with probability 1/2. Apply the algorithm recursively to H,
producing a minimum spanning forest F of H. Find all the F-heavy edges
(both those in H and those not in H) and delete them from the contracted
graph.
3. Apply the algorithm recursively to the remaining graph to compute
a spanning forest F‘. Return those edges contracted in Step (1) together
with the edges of F‘.
```
[link](https://dl.acm.org/citation.cfm?doid=201019.201022)
##### Bernard Chazelle's Algorithm
```
[1] If t = 1 or n = O(1), return MSF (G) by direct computation.
[2] Perform c consecutive Boruvka phases.
[3] Build K and form the graph B of bad edges.
[4] Set F <- U msf(Cz \ B, t - 1) for z belong to K
[5] Return msf(F ł B, t) U {edges contracted in Step [2]}
```
[link](https://dl.acm.org/citation.cfm?id=355562)
#### 2 status_check
(a)解决interval schedule 问题的过程中间, 可以最优解包含的interval和与该 interval 冲突的 
intervals, 只需要在冲突区间交集即可,算法的伪代码为:
```
sort the intervals by end time
init variable last_interval = first value in sorted_intervals
remove first value of sorted_intervals
init an empty map M
init an empty set S
for interval in sorted_interval:
    if interval is conflict with last_interval
        put kv = (interval, last_interval) to M
    else
        last_interval = interval
        add interval to S
for interval in S
    print the end time of S
```

(b) 由于k\* 个process 标记为 P 两者之间没有相交,所以至少为k\*个,  
使用上一问的算法, 最多只可以k\*个不相交的process, 只需要证明该算法产生的确可以实现检测所有的
process:  
1. 对于选定的process的集合,显然被检测到, 应为检测点为process 的结束的时间
2. 对于未被选定的 process A, 根据M,可以知道和他冲突的 的process B. B的结束时间和早于 A的结束
时间的, 如果A 的开始时间也是晚于B的结束时间, 那么Map 中间不会有, (A, B)这样的键值对, 所以
A 必定会和B的结束时间点重叠, 所以B的监测点同时可以检测 A
3. 综合1 2,可以知道会检查所有的节点

#### 3 Prove the relationship of height and cardinality
证明: 
1. 对于只有一个节点的tree , 成立
2. 如果对于高度小于k(k>=2)的tree, 如果都是满足k <= log(capacity(tree)) + 2, 假定含有两个tree A
和 B , 两者的高度为 Ha 和 Hb, 节点的数目为 Ca 和 Cb 现在分为一下2种情况讨论,
 a. 如果Ha > Hb,那么产生的新tree的为 Ha, 由于Ha <= log(Ca) + 2, 所以 Ha <= log(Ca + Cb) + 2
b. 如果Ha = Hb ,那么产生的新tree的高度为 Ha + 1, 由于 Ha <= log(Ca) + 2  Ha <= log(Cb) + 2
所以 Ha <= log(Ca + Cb)/ 2 + 2 = log(Sqrt(Ca + Cb) * 2) + 1 <= log(Ca + Cb) + 1
即为 Ha <= log(Ca + Cb) + 1, Ha + 1 <= log(Ca + Cb) + 2
3. 综合以上两部,可以说明正确性


#### 4 More on MST
考虑一种情况,所有的边的weight 都是相同的, 此时寻找MST的最简单的方法为 BFS,复杂度 O(V + E), 
由于是完全串行的,所以span也是 O(V + E), 需要找到一个并行度更加高的算法：　　
猜想：　
1. 由于所有的边的权重相同，所以只是需要将所有的环路删除即可
2. 可以使用 red blue 算法, 使用循环red 添加边, 而blue 删除构成环路的边
3. 借用 Borukva 的想法, 对于segment A随机的添加一条边 E = (A, B), 而且保证B 包含的边只有
E, 如此就可以保证每一轮添加的边不会构成环.

现在分析想法3:
a. 如果保证不会出现cycle, 按照1/2 的概率选定中心节点,标记为H, 如果为非中心节点, 那么标记为C,
 在每一轮所有的H节点按照相同的概率添加所有的一条边,这一条边的另外一段为C节点, 
b. 现在说明使用a中间的方法不会产生一个 cycle: 如果出现了环路, 那么环路上面的节点只会交替出现,
应为按照a 中间的规则, 边的两端只有H 和 C, 如果是交替出现, 那么意味着 一个 H 和 两个Ｃ 相连接
，　但是　Ｈ只会选择一条边，　所以说明不会构成环路
ｃ. 算法的复杂度和 BFS相同, 但是span有较大的下降,取决于图的本来的结构

伪代码:
```
graph is G, vertexes and edges are V and E
init a forest F with segment are V
while F has more than one segment
    label every vertex H or C in 1/2 probability
    for every vertex H find edge e with equal probability connecting it's C neighbors
    add e to F
```