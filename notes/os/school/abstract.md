os: 并发 共享 不确定性


Concurrency means that two or more calculations happen within the same time frame, and there is usually some sort of dependency between them.

Parallelism means that two or more calculations happen simultaneously.


处理机的特权级(态)
定义: 中央处理机的工作状态
目的:保护操作系统内核
supervisor mode --- 全部指令 和 全部资源
user mode --- 没有特权指令 不可以直接取用资源 改变处理的状态

中断及其处理:
exception + IRQ + sysCall => Interrupt
exception IRQ 区别:
1. IRQ 异步发生的, exception 当前的程序发生,为同步; 
2. IRQ 可以关闭, 但是 exception 无法关闭
3. IRQ 返回位置在下一条指令, exception 发生在当前的指令


必要的硬件支持: 
DMA(Direct Memory Access)(主板)
1. cpu => dma controller with parameter(address count control)
2. mda => disk controller => IRQ
3. data transfer
4. dc(disk controller) ack to dma
5. IQR

时钟 : 
2. 可编程间隔定时器(programable interval clock)
3. 时间戳计数器 TSC

操作系统
1. 工作环境
    1. 系统引导
       rom bios => device enumeration => boot loader(磁盘开始位置) => kernel 
    2. 系统生成
2. 运行一个应用程序的过程
3. 操作系统用户界面
4. 系统功能调用

linker -> symbol => virtual address
loader - > virtual address => physical address

static link -> exe 文件很大
dynamic link -> 依赖环境

命令接口
程序接口

1.1 主要特点: 顺序性
1.2 批处理: a. 人工干预, 多用户
1.3 设计目标 设计的方法
1.4 
1.5 独立
1.6 cpu 的时间分成若干, 时间片给若干程序
1.7 向下控制硬件, 向上提供接口



顺序:
顺序性
封闭性
可再现

虚拟化: 时间虚拟化 空间虚拟化

并发:
程序的封闭和可再现
程序和计算不在一一对应:程序持有多个计算
程序并发执行的相互制约

data race : 出现一个写

进程描述: 给定空间 和资源的执行的过程
1. PCB process control block :
    1. 进程标识符
    2. 进程当前的状态
    3. 当前队列指针
    4. 进程的优先级
    5. and so on

2. 进程之间的相互作用
    1. 临界资源:  一次只有一个进程可以使用的 critical resource
    2. 临界区: 对于公共变量审查和修改的 critical section
    3. 互斥: 进程之间 一个人持有的时候, 其他的人不允许读写 mutual exclusion

    4. 同步 : 相互等待 互通消息 coordination/ synchronization
        1. 发生关系对象
        2. 互相等待的关系
    5. 互斥为特殊的同步,两者都是进程之间相互制约关系 

3. 进程的同步机构
    1. 锁 atomic operation 
    2. 信号灯 (s, q) s 非负初值, 初值为负数, 表示开始的时候等待队列不为空
        1. p 操作 : 可能的导致阻塞, -1, 小于0, 进入等待,  对于调用者本身作用,变成等待态,  调用p 的进入信号灯等待队列中间
        2. v 操作 : 不会导致阻塞, 影响已经在信号灯上面的等待者, v(s) 信号灯数值 +1, 结果 <=0, 那么唤醒信号灯等待队列上面的进程
        3. p v为原语, 如果


4. 进程互斥和同步的实现
上锁的实现: 轮询 的方式实现, 所以
锁 advantage: 如果临界区域小的时候, 型号灯的信号灯的状态变化导致资源的消耗
锁 disadvantage: 如果临界区域大, 轮询 浪费

    1. 定义信号灯
    2. coBegin coEnd 的定义
    3. Pi(){}

5. IPC 信箱通信

6. 线程
创建子进程: fork 需要创建PCB
A code stack data => B code(not copy) stack(new) data(copy) 

创建子线程: pThread.create 不一定需要创建PCB user-level kernel-level(Linux)
A code stack data => B code(not copy) stack(new) data(share)

conclude: difference thread can change the parent data
线程之间的通信可以共享地址区域 和 ???

7. 进程调度: 非剥夺方式 和 剥夺方式
    
8. [哲学家进餐问题](https://en.wikipedia.org/wiki/Dining_philosophers_problem#Solutions)

9. 读者写者问题 


# 资源分配与调度

# 死锁问题
死锁产生的必要条件:　互斥条件　不剥夺条件　部分分配　环路条件

prevent 
avoid
solute => detection solution 


分区分配: 
碎片 + 拼接
vma =virtual memory address
slab allocator


分区物理使用: 分页 
虚地址: 分区非配

分页: 程序地址空间被分为大小相等的片, 成为虚页
主存块: 实页

page table : 页表
page table entry: 页表项

TLB translation lookaside buffer: (联想缓冲器)

请求页面的机制: 简单 和 请求 
缺页处理: exception

thrashing : 主存和辅存之间的页面置换现象

缺页中断率

淘汰算法: LRU OPT FIFO

段式地址 二维空间

flat mode

pfn: page frame number  

##　设备管理
设备分类

设备的管理目标：
1. 提高设备利用率
2. 方便用户的使用

设备独立性: 逻辑设备名 物理设备名

设备控制块: 缓存技术, 实现平滑的传输过程

## 文件系统

文件: 文件名 完整信息  **and**
.a .so lib  lib64

物理记录: 在存储介质上面, 由连续信息锁组成的一个区域叫做块, 称为物理记录

流式文件: 有序字符的集合, 无结构
记录式文件: 有结构

定长:
变长:

## 伙伴算法


## Review
脱机 和 联机 的定义

