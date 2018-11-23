Theoretical and empirical evidence indicates that the depth of neural networks
is crucial for their success.

## 1 Introduction & Previous Work
> 介绍之前的人做的工作 处理

## 2 Highway Networks
y = H(x; WH)· T(x; WT) + x · C(x; WC)

We refer to T as the transform gate and C as the carry gate, since they express how much of the
output is produced by transforming the input and carrying it, respectively. For simplicity, in this
paper we set C = 1 − T, giving

### 2.1 Constructing Highway Networks
To change the size of the intermediate representation, one can replace
x with ^x obtained by suitably sub-sampling or zero-padding x

Another alternative is to use a plain
layer (without highways) to change dimensionality, which is the strategy we use in this study


Convolutional highway layers utilize weight-sharing and local receptive fields for both H and T
transforms. We used the same sized receptive fields for both, and zero-padding to ensure that the
block state and transform gate feature maps match the input size

### 2.2 Training Deep Highway Networks
This suggests a simple initialization scheme which is independent of the nature of H: bT can be initialized with a negative value (e.g. -1, -3 etc.) such that the network is initially biased towards carry behavior.

In our experiments, we found that a negative bias initialization for the transform gates was sufficient for training to proceed in very deep networks for various zero-mean initial distributions of WH and different activation functions used by H.
