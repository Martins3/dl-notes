A number of interesting things follow from this, including fundamental lower-bounds on the complexity of a neural network capable of classifying certain datasets.

This perspective will allow us to gain deeper intuition about the behavior of neural networks and observe a connection linking neural networks to an area of mathematics called topology.

## A Simple Example
## Continuous Visualization of Layers

## Topology of tanh Layers
Each layer stretches and squishes space, but it never cuts, breaks, or folds it,transformations like this, which don’t affect topology, are called homeomorphism,formally, they are bijections that are continuous functions both ways.

## Topology and Classification
Consider a two dimensional dataset with two classes A,B⊂R2A,B⊂R2:
A={x|d(x,0)<1/3}
B={x|2/3<d(x,0)<1}
Claim: It is impossible for a neural network to classify this dataset without having a layer that has 3 or more hidden units, regardless of depth.

> 体会： homeomorphism 的定义 而且仅仅只是需要nonsingular matrix 的 W 就可以，amazing
> topology 用来分析的classification的问题说明了，维度 拓扑变换和hidden的关系


> 想法： 神经网络含有那么多层数，那么如何确定上一层和下一层的hidden unit的数目关系，还有的就是，按照文章的解释，那不是unit的数目越多越好（不考察计算复杂度），或者如果找到问题所需要的最小的hidden unit 的数目有没有被解决

## The Manifold Hypothesis
The manifold hypothesis is that natural data forms lower-dimensional manifolds in its embedding space

> embedding space 和 manifold 是什么 ？

## Links And Homotopy
In topology, we would call it an ambient isotopy between the original link and the separated ones.

---
搞个铲铲，看不懂啊
