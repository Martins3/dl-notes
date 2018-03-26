# Network Flow

One of the oldest problems in combinatorial algorithms is that of determining the size of the largest matching in a bipartite graph G. (As a special
case, note that G has a perfect matching if and only if |X| = |Y| and it has a
matching of size |X|.) This problem turns out to be solvable by an algorithm
that runs in polynomial time, but the development of this algorithm needs
ideas fundamentally different from the techniques that we’ve seen so far.
> 真的不是很懂什么叫做largest matching 啊 !

##  1 The Maximum-Flow Problem and the Ford-Fulkerson Algorithm
> second, that there is at least one edge incident to each node 什么意思 P339
f(e): two restriction
v(f):
The Maximum-Flow Problem: Given a flow network, find a flow of maximum possible value
As a bonus, our algorithm will also compute the minimum cut

We can push forward on edges with leftover capacity, and we can push backward on edges that are
already carrying flow, to divert it in a different direction

The Residual Graph:
1. The node set of Gf is the same as that of G.
2. For each edge e = (u, v) of G on which f(e) < Capacity(e), there are Capacity(e) − f(e) “leftover” units of capacity on which we could try pushing flow forward.So we include the edge e = (u, v) in Gf, with a capacity of Capacity(e) − f(e). We will call edges included this way **forward edges**.
3. For each edge e = (u, v) of G on which f(e) > 0, there are f(e) units of flow that we can “undo” if we want to, by pushing flow backward. So we include the edge e_ = (v, u) in Gf, with a capacity of f(e). Note that e_ has the same ends as e, but its direction is reversed; we will call edges included this way **backward edges**.

> 简单来说就是: residual graph 的需要首先指定 f
capacity of an edge in the **residual graph** as a residual capacity, to help distinguish it from the capacity of the corresponding edge in the original flow network G.

augmenting paths in a residual path
 