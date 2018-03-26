1. 优化图形生成的方案
2. 生成更加大图形, 即使只有8个 labels ,人都是难以区分清除的, 感觉需要增加一倍的大小
3. 使用cnn的模型进行分类
4. 不适用规则的图形, 而是使用非规则的矩形

1. 生成矩形的数目


1. 进一步可以处理的为: 如果生成的多边形是人没有办法理解,那么是不是还是含有这样高的精度

1. 如果小圆 可以很好的识别, 大圆也是可以很好的识别, 混合之后就是难以识别, 那么是不是就是很尴尬
那么就是可以探索之间的关系

2. 不使用 mean, 而是使用 sum


4. 在 cloud 上面计算出来的 测试集合和 train 的精度居然总是交缠在一起的, 不是bug 就是 值得思考的部分, 说明是能力不够吗 ? 使用更加缓和的full来构建网络吗 ?


5. 如果修改模型, 那就是直接使用resnet 或者 stochastic networks 进行计算的
> tensorflow 的官方提供了部分的modle的部分, model的使用不是十分的清楚, [personal code](https://github.com/xuyuwei/resnet-tf)感觉还是很简单的,明天操作一波查看一下效果如何

6. 有一件很有意思的事情: 那就是既然training accurate 已经到达99, 为什么测试只有70, 增加一个全连接之后
模型变得复杂,反而generation 变的更加好了, generation 必定没有想象的那么简单

7. 为什么step_size 需要设置的这么小才可以, 而且交换模型之后, 对于step_size的设置的变化瞬间变化

8. 一个玄学的事情就是: 不要使用太宽的, 使用将狭窄的转换更加深,往往可以得到更加好的结果




## Two
对于VGG 使用 噪音图 输出结果


## SVD / PCA 分析
use sk-learn and then use a less graph
1. how can we compare the ability with them !
2. 