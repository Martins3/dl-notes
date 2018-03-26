## abstract
Despite their massive size, successful deep artificial neural networks can exhibit a
remarkably small difference between training and test performance
> 放屁， 为什么参数的个数就是必须和训练的样本的数目更加少
> 什么叫做 small difference , 使用方差老衡量的吗？ 还是别的什么东西 ？

## 1 INTRODUCTION
To answer such a question, statistical learning theory has proposed a number of different complexity measures that are capable of controlling generalization error. These include VC dimension (Vapnik,
1998), Rademacher complexity (Bartlett & Mendelson, 2003), and uniform stability (Mukherjee
et al., 2002; Bousquet & Elisseeff, 2002; Poggio et al., 2004). Moreover, when the number of
parameters is large, theory suggests that some form of regularization is needed to ensure small
generalization error. Regularization may also be implicit as is the case with early stopping.
> 核心问题之一: What is it then that distinguishes neural networks that generalize well from those that don’t?

### 1.1 OUR CONTRIBUTION
In this work, we problematize the traditional view of generalization by showing that it is incapable
of distinguishing between different neural networks that have radically different generalization performance

Deep neural networks easily fit random labels

> 根据文章的说法，也就是使用randomlize的labels的时候，训练的时间更加长 ？ 为什么会有这一种想法

We observe a steady deterioration of the
generalization error as we increase the noise level

This shows that neural networks are able to
capture the remaining signal in the data, while at the same time fit the noisy part using brute-force


Explicit regularization may improve generalization performance, but is neither necessary nor by
itself sufficient for controlling generalization error

It appears to be more of a tuning parameter that often helps improve the final test error
of a model, but the absence of all regularization does not necessarily imply poor generalization error

#### Finite sample expressivity
our result shows that even depth-2 networks of
linear size can already represent any labeling of the training data

#### The role of implicit regularization
While explicit regularizers like dropout and weight-decay
may not be essential for generalization, it is certainly the case that not all models that fit the training
data well generalize well
> explicit regularizers 到底是什么 ？

### 1.2 RELATED WORK
Our results show that even empirically training neural
networks is not uniformly stable for many passes over the data
> uniform stable ?  many pass over the data

All of these results are at the population level characterizing which mathematical functions
certain families of neural networks can express over the entire domain. We instead study the representational power of neural networks for a finite sample of size n. This leads to a very simple proof
that even O(n)-sized two-layer perceptrons have universal finite-sample expressivity

This leads to the question of whether there is a different form of capacity control that bounds generalization error for large neural nets.

## EFFECTIVE CAPACITY OF NEURAL NETWORKS
Our goal is to understand the effective model capacity of feed-forward neural networks


> Whatever justification we had for expecting a small generalization
error to begin with must no longer apply to the case of random labels 这是啥 ？


To gain further insight into this phenomenon, we experiment with different levels of randomization
exploring the continuum between no label noise and completely corrupted labels. We also try out
different randomizations of the inputs (rather than labels), arriving at the same general conclusion.

### 2.1 FITTING RANDOM LABELS AND PIXELS
