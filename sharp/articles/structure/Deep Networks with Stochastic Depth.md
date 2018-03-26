## Abstract
 Very deep convolutional networks with hundreds of layers
have led to significant reductions in error on competitive benchmarks.
> 先看完的 rethink generzation 之后，表示这一句话是没有的cite 任何的文章， 根本不可靠

To address these
problems, we propose stochastic depth, a training procedure that enables
the seemingly contradictory setup to train short networks and use deep
networks at test time.
> kernel
> 而且这一个anti intuition 的， 如果是训练的时候分开训练，组合起来如何保证好的效果
> 相同的问题应该是从 dropout 开始的
> layer wise gready training

We start with very deep networks but during training, for each mini-batch, randomly drop a subset of layers and bypass
them with the identity function.
> 看来参差的想法的确是影响深远， 都是采用这一种观点来说明的

## 1 Introduction


Network depth is a major determinant of model expressiveness, both in theory [9, 10] and in practice [5, 7, 8]. However, very deep models also introduce
new challenges: vanishing gradients in backward propagation, diminishing feature reuse in forward propagation, and long training time.
Vanishing Gradients is a well known nuisance【招人讨厌的东西】 in neural networks with many
layers [11].
> 如果有时间的话， check 一下为什么上面引用的文章，然后从哪里开始说 深度越深 效果越好的说法


As the gradient information is back-propagated, repeated multiplication or convolution with small weights renders the gradient information ineffectively small in earlier layers. Several approaches exist to reduce this effect in
practice, for example through careful initialization [12], hidden layer supervision
[13], or, recently, Batch Normalization [14].
> 三个文章， 几乎所有的文章对于这一个都是含有引用的
> Batch Normalization 为什么可以 让 very deep network 的training become possible

Diminishing feature reuse during forward propagation (also known as loss in
information flow [15]) refers to the analogous problem to vanishing gradients in
the forward direction.


 Recently, several new architectures attempt to circumvent this problem through direct identity mappings
between layers, which allow the network to pass on features unimpededly from
earlier layers to later layers [8, 15].

> 这一个文章在这里瞎几把黑残差网络，说需要几个星期才可以收敛，可以回到参差的网络中间review 一下，是不是这样的
> 从这一个位置开始就是对于参差对于他的搞法的解释 已经变成了将信息直接的传送


The reduction in training time can be attributed to the shorter forward and backward
propagation, so the training time no longer scales with the full depth, but the
shorter expected depth of the network. We attribute the reduction in test error
to two factors
1) shortening the (expected) depth during training reduces the
chain of forward propagation steps and gradient computations, which strengthens the gradients especially in earlier layers during backward propagation;
2)networks trained with stochastic depth can be interpreted as an implicit ensemble of networks of different depths, mimicking the record breaking ensemble of depth varying ResNets trained by He et al. [8].


## 2 Background

Many attempts have been made to improve the training of very deep networks.



Residual networks (ResNets)[8] simplify Highway Networks by shortcutting
(mostly) with identity functions.

> pass gradient and features 这两个东西都是说的很轻巧，但是实际上根本就是不知道为什么的

Dropout. Stochastically dropping hidden nodes or connections has been a
popular regularization method for neural networks



 Anecdotally, Dropout loses effectiveness when used
in combination with Batch Normalization [14, 23]. Our own experiments with
various Dropout rates (on CIFAR-10) show that Dropout gives practically no
improvement when used on 110-layer ResNets with Batch Normalization.
> 天池的比赛的结果显示，实际上不是如此的，no improvement, 绝对不可能是no improvement的东西

## 3 Deep Networks with Stochastic Depth

> 蛇皮啊，就是在 resNet 的基础上面的 添加一个Stochastic 然后就是随机深度，代码都不用修改几行
#### ResNet architecture
>  bottleneck block 在 ResNet 里面含有详细的描述，看来需要看一看

#### Stochastic depth
H = ReLU(b * f(Hl) + id(Hl))
Hl means last H, only difference is b means probability

#### The survival probabilities
We conclude that the linear decay rule  is
preferred and, as training with stochastic depth is surprisingly stable with respect
to pL, we set pL = 0.5 throughout

#### Expected network depth
3/4 when linear decay pL = 0.5
#### Training time savings

#### Implicit model ensemble
One explanation for our performance improvements
is that training with stochastic depth can be viewed as training an ensemble
of ResNets implicitly.
> one explanation, 看来是自己也是解释不清楚的

## 6 Conclusion
