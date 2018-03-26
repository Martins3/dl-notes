## Abstract
> 也许回头看这一个问题的时候理解会更加深刻

## 1. Introduction
Yet deep neural networks (DNNs) often achieve excellent generalization performance with massively over-parameterized models. This phenomenon is not well-understood

From a representation learning perspective, the generalization capabilities of DNNs are believed to stem from
their incorporation of good generic priors

### Main Contributions
We operationalize the definition of “memorization” as the
behavior exhibited by DNNs trained on noise, and conduct
a series of experiments that contrast the learning dynamics
of DNNs on real vs. noise data

Our findings are summarized as follows:
1. There are qualitative differences in DNN optimization
behavior on real data vs. noise. In other words, DNNs
do not just memorize real data.
2. DNNs learn simple patterns first, before memorizing.In other words, DNN optimization is
content-aware, taking advantage of patterns shared by
multiple training examples.
3. Regularization techniques can differentially hinder
memorization in DNNs while preserving their ability
to learn about real data

## 2. Experiment Details

## 3. Qualitative Differences of DNNs Trained on Random vs. Real Data
In particular, our experiments highlight some qualitative differences between DNNs trained on real data vs. random data, supporting the fact that DNNs do not use brute-force memorization to fit real datasets

### 3.1 Easy Examples as Evidence of Patterns in Real Data
A brute-force memorization approach to fitting data should
apply equally well to different training examples. However, if a network is learning based on patterns in the data,
some examples may fit these patterns better than others.


> 由于的元素更加容易被区分，那也就是说在特征空间，有的元素更加容易放置到一个好的位置
> 难道这不是很好解释的吗 ? 应因为分布的空间的是相似的，而不是将所有的全部都是记住，而是将对应的空间记住
> figure 2 的randX randY 区别的使用无法解释 ？ 测试集 使用是新的数组吗？

### 3.2. Loss-Sensitivity in Real vs. Random Data
