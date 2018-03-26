count the object in the picture
[website](http://www.robots.ox.ac.uk/~vgg/research/counting/)
[the pdf](https://www.robots.ox.ac.uk/~vgg/publications/2010/Lempitsky10b/lempitsky10b.pdf)

1. count object has been done, 有意思的是: 如果事先可以训练的结果是0 ~9, 如果之后提供的10 ,所对应的输出的应该是什么
我们有没有对于任意的多的数目的圈都是可以的实现 分类的

并不是的,应该还是被做过,应该还是对于任意的数值都是可以count的
但是可以做的,如果 使用不同的数值,那么是不是可以 训练是不是的含有区别


2. 有没有可能得到的结果是两个网络, 一个用于指定到底是哪一个object, 第二个用于count 个数,来实现对于任何的个数实现的

3. 一个可以比较小的 在count objetc 的时候, 结果就是可以比较的不同的表示 训练的时候 有没有什么区分 的不同的,变化的为阿拉伯数字 线条


4. 标签不在是数字,而是使用 关系 ,使用使用图片组合的形式
可以创建数据集,也是可以的从 MNIST 的基础上面开始
如果真的可以学习 relationship ,那么有没有可能对于学习到的 relationship 生成对应的数值
/home/martin/AllWorkStation/Atom/sharp/articles/abstraction/A neural approach to relational reasoning.md 这一部分可以参考

5. 拼图, 生成新的拼图从的 原来的内容中间的,可以相同的分割,也是可以不相同的分割的方法
<!-- 如果可以从零碎的图片中间整合图片 ,那么是不是也是可以 用多个图片生成 很高的解析度的 图片的 -->

拼图: 是不是可以实现拼装的判断

拼图的问题 是不是可以变成的 提供两个图片的,一个是 甜甜圈 一个是 饼子, 那么查看检查相同的数目的图像


6. 如果使用 矩形 进行数字的学习, 然后使用圆形测试, 会不会有相同的得到的结果

7. 计算 five_star 的时候,  如果网络学会了, 那么他是通过面积得到的, 还是通过
