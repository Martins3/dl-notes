## Abstract
We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual
networks are easier to optimize, and can gain accuracy from
considerably increased depth.
> reference function and unreferenced function confused at reference ?



## 1. Introduction
Deep networks naturally integrate low/mid/highlevel features  and classifiers in an end-to-end multilayer fashion, and the “levels” of features can be enriched by the number of stacked layers (depth).
> 此处cite 的文章 很酷


When deeper networks are able to start converging, a
degradation problem has been exposed: with the network
depth increasing, accuracy gets saturated (which might be
unsurprising) and then degrades rapidly. Unexpectedly,
such degradation is not caused by overfitting, and adding
more layers to a suitably deep model leads to higher training error
> 如果不是由于的overfitting 造成的， 那么到底是什么造成的 ？
> 之所以说是不是由于的 overfitting 造成是因为training error and test error 同时出现了较大的增加

Formally, denoting the desired
underlying mapping as H(x), we let the stacked nonlinear
layers fit another mapping of F(x) := H(x) −x. The original mapping is recast into F(x)+x. We hypothesize that it
is easier to optimize the residual mapping than to optimize
the original, unreferenced mapping. To the extreme, if an
identity mapping were optimal, it would be easier to push
the residual to zero than to fit an identity mapping by a stack
of nonlinear layers

## 2. Related Work
__Residual Representations__. In image recognition, VLAD
[18] is a representation that encodes by the residual vectors
with respect to a dictionary, and Fisher Vector [30] can be
formulated as a probabilistic version [18] of VLAD. Both
of them are powerful shallow representations for image retrieval and classification [4, 48]. For vector quantization,
encoding residual vectors [17] is shown to be more effective than encoding original vectors.
In low-level vision and computer graphics, for solving Partial Differential Equations (PDEs), the widely used
Multigrid method [3] reformulates the system as subproblems at multiple scales, where each subproblem is responsible for the residual solution between a coarser and a finer
scale. An alternative to Multigrid is hierarchical basis preconditioning [45, 46], which relies on variables that represent residual vectors between two scales. It has been shown
[3, 45, 46] that these solvers converge much faster than standard solvers that are unaware of the residual nature of the
solutions. These methods suggest that a good reformulation
or preconditioning can simplify the optimization.
__Shortcut Connections__. Practices and theories that lead to
shortcut connections [2, 34, 49] have been studied for a long
time. An early practice of training multi-layer perceptrons
(MLPs) is to add a linear layer connected from the network
input to the output [34, 49]. In [44, 24], a few intermediate layers are directly connected to auxiliary classifiers
for addressing vanishing/exploding gradients. The papers
of [39, 38, 31, 47] propose methods for centering layer responses, gradients, and propagated errors, implemented by
shortcut connections. In [44], an “inception” layer is composed of a shortcut branch and a few deeper branches.
Concurrent with our work, “highway networks” [42, 43]
present shortcut connections with gating functions [15].
These gates are data-dependent and have parameters, in
contrast to our identity shortcuts that are parameter-free.
When a gated shortcut is “closed” (approaching zero), the
layers in highway networks represent non-residual functions. On the contrary, our formulation always learns
residual functions; our identity shortcuts are never closed,
and all information is always passed through, with additional residual functions to be learned. In addition, high
> 相关的没有看， 也看的不是很懂的

## 3 3. Deep Residual Learning

### 3.1. Residual Learning
Let us consider H(x) as an underlying mapping to be
fit by a few stacked layers (not necessarily the entire net),
with x denoting the inputs to the first of these layers.
> H(x) 表示为好几层集合







Although both forms should be able to asymptotically approximate the desired functions (as hypothesized),
the ease of learning might be different.
This reformulation is motivated by the counterintuitive
phenomena about the degradation problem (training error 反而更加高).


As we discussed in the introduction, if the added layers can
be constructed as identity mappings, a deeper model should
have training error no greater than its shallower counterpart.

The degradation problem suggests that the solvers
might have difficulties in approximating identity mappings
by multiple nonlinear layers.
> 这一句话的说法是有问题的，如果含有difficultie, 那么就是说明autoencoder不想要的情况f(x) = x 是一件很简单的事情


 With the residual learning reformulation, if identity mappings are optimal, the solvers
may simply drive the weights of the multiple nonlinear layers toward zero to approach identity mappings.

In real cases, it is unlikely that identity mappings are optimal, but our reformulation may help to precondition the
problem.
 If the optimal function is closer to an identity
mapping than to a zero mapping, it should be easier for the
solver to find the perturbations with reference to an identity
mapping, than to learn the function as a new one.
> 难道就是为了解决一个identity map 相比较 映射为0 map 更加的麻烦吗 ？

We show by experiments (Fig. 7) that the learned residual functions in
general have small responses, suggesting that identity mappings provide reasonable preconditioning
### 3.2. Identity Mapping by Shortcuts
 Formally, in this paper
we consider a building block defined as:
y = F(x; Wi) + x: (1)

The dimensions of x and F must be equal in Eqn.(1).
If this is not the case, we can perform a linear projection Ws by the
shortcut connections to match the dimensions:
y = F(x; Wi) + Wsx: (2)


We can also use a square matrix Ws in Eqn.(1). But we will
show by experiments that the identity mapping is sufficient
for addressing the degradation problem and is economical,
and thus Ws is only used when matching dimensions.

The form of the residual function F is flexible. Experiments in this paper involve a function F that has two or
three layers, while more layers are possible.



### 3.3. Network Architectures



### 3.4. Implementation



## 4. Experiments
```
以后再说，个人觉得这也可以成为你best paper, 搞笑
```
