Deformable convolution
怎样才能减少卷积层参数量？-- Bottleneck : ResNet 提出的
每层卷积只能用一种尺寸的卷积核？-- Inception结构
能否让固定大小的卷积核看到更大范围的区域？-- Dilated convolution
通道间的特征都是平等的吗？ -- SEnet
分组卷积能否对通道进行随机分组？-- ShuffleNet
卷积操作时必须同时考虑通道和区域吗？-- DepthWise操作

卷积核方面：
大卷积核用多个小卷积核代替；
单一尺寸卷积核用多尺寸卷积核代替；
固定形状卷积核趋于使用可变形卷积核；
使用1×1卷积核（bottleneck结构）。

卷积层通道方面：
标准卷积用depthwise卷积代替
使用分组卷积；
分组卷积前使用channel shuffle
通道加权计算。

卷积层连接方面：
使用skip connection，让模型更深；
densely connection，使每一层都融合上其它层的特征输出（DenseNet）

1. CNN 起源的文章
2.
```
其实，既然有人可以写一篇文章关于generation, 那么为什么不写一个 rethink CNN， 感觉也不是有很多人对于CNN的原理含有一个很清楚的了解啊 ！

如果所谓的扩大的 视线 和 改变kernel 的形状的 的效果没有没有得到应有的结果，那么就是需要回想，是不是CNN的设计就是原本来的那样的

没有人 关注 CNN 的 history 吗 ？ 这一个东西显得如此的突如其来，没有人觉得很奇怪吗 ？
```
