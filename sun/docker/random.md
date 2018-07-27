1. Docker可以解决虚拟机能够解决的问题，同时也能够解决虚拟机由于资源要求过高而无法解决的问题.
2. Docker两个最重要的概念是 *镜像* 和 *容器*。除此之外，*链接* 和 *数据卷* 也很重要。我们先从镜像入手。


1. docker image pull alpine  获取docker image alpine(linux 发行版)
2. docker image ls 打印所有的image   
3. docker container run alpine ls -l 运行 alpine 并且执行 ls -l
4. docker container ls  打印已经运行过的container, -a 表示曾经运行过的image
5. 
