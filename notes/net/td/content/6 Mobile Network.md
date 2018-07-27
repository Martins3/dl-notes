# 概述
1. 两个重要的挑战:  
无线特性：基于无线链路的通信；  
移动特性：移动用户的网络接入点是变化的。
2. 无线链路  
典型的作用是用于连接无线主机和基站;  
也可以用于骨干链路 ；  
与链路访问相匹配的多址访问协议；  
多种数据传输速率和传输距离  
3. 无线局域网可分为两大类:有固定基础设施和自组网络(ad hoc 网络) 。


4. 无线网络的元素: 无线主机, 无线链路 基站
5. 关联 切换
6. 无线链路的特征  
    1. 递减的信号强度  
    2. 来自其他源的干扰  
    3. 多径传播  
    所以更加容易出错
    
7. 采用`CRC`进行帧校验(组原)  
采用`ARQ`协议进行重传  
the types of ARQ protocols include Stop-and-wait ARQ, Go-Back-N ARQ, and Selective Repeat ARQ 

8. BER SNR
9. 隐藏终端问题:  
    1. 含有障碍物
    2. 信号衰减
10. [CDMA](https://en.wikipedia.org/wiki/Code-division_multiple_access)  
    1. 所有用户含有自己的 mbit
    2. 站点发送1 为 mbit , 发送0 , mbit 的反码
    3. 不同站点的 CDMA 码片相互正交
11. 802.11 协议簇


12. 802.11 协议架构: 无线终端通过AP(Access Point)进行通信

13. 802.11b的信道划分: 11个 相隔四个没有干扰
14. 802.11b主机关联 AP的过程: 
    1. 每个AP周期性发送信标帧，包括AP的 SSID(Service Set Identifier) 和MAC
    2. 主机对11个信道进行扫描，获取所有可用的AP的信标帧
    3. 主机选择其中一个AP进行关联，加入其所属子网
    4. 主机向关联 AP 发送 DHCP 发现报文，获取IP地址 可能需要身份鉴别

15. 802.11的MAC protocol
    1. broadly speaking there are three classes of multiple access protocols: channel partitioning (including CDMA), random access, and taking turns.
    2. First, instead of using collision detection, 802.11 uses *collision-avoidance techniques*. Second, because of the relatively high bit error rates of wireless channels,
802.11 (unlike Ethernet) uses a *link-layer acknowledgment/retransmission* (ARQ)
scheme

16. 

    
## Question
1. 对于给定的SNR，具有较高比特传输率的调制技术将具有较高的BER(比特传输速率没有关系才对,只是传输的时间短而已)

2. As with Ethernet’s CSMA/CD, the “CSMA” in CSMA/CA stands for “carrier sense multiple access,”
meaning that each station senses the channel before transmitting, and refrains from
transmitting when the channel is sensed busy

16. 802.11 不采用冲突检测原因, PPT 20页 一直到后面需要等到 Esternet 的部分的完成之后处理
17. 移动管理:
    1. 概念
        1. 归属网络:
        2. 归属代理: 当移动用户在远程时,代表移动节点执行移动管理功能的实体.
        3. 永久地址: 归属网络中的地址,用它一定可以找到 移动用户
        4. 被访问网络: 移动用户当前所在的网络
        5. 转交地址（COA）: 在被访问网络中的地址
        6. 外部代理: 在被访问网络中帮助移动节点完成移动管理功能的实体. 
    2. 移动性处理办法:
        1. 路由器处理: 本访问网络 向外 广播该节点永久地址
        2. 终端处理
            1. 归属代理首先截获该数据报, 然后通过移动用户的COA将数据报转发给外部代理，然后从该外部代理转发给移动用户。
            2. 通信者获取移动用户的外部地址, 然后直接将数据报发给移动用户

18. 移动节点的注册
    1. 
    

19. 移动管理
    1. 移动节点的间接选路算法: 让归属代理辅助
    2. 移动节点的直接选路算法: 从归属代理获取外部地址
        1. 如果节点切换到了新的网络中间, 如何处理 ? Anchor foreign agent(锚外部代理)

20. 支持移动性的因特网体系结构与协议统称为移动IP（RFC3220）

21. 移动标准的组成(**需要中文资料**)
    1. 代理发现
        1. 
    2. 向归属代理注册
        1. 
    3. 数据报的间接路由
        1. 归属代理向外部代理发送的数据报: 原始数据报封装在一个新数据报内

 

22. 无线和移动 对于高层影响:
    1. 逻辑小
    2. 性能大
