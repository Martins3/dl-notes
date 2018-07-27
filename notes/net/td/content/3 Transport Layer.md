# 问题
1. ATM ABR 说明的是什么 ?
2. TCP重传为混合体, 具体如何混合的 ?
3. TCP的控制:
    1. 冗余的ACK 会不会增加 cwnd : *Ans* 会, 所以为ssthresh + 3 = cwnd
    3. 由于是每一个rtt的时间中间, 如何测定rtt 的时间 ?
    4. 在慢启动的时候, 如果ssthresh 为12, 那么 cwnd 是直接跳到 16 还是 12 ?
4. 不同的主机, 相同主机号, 发送到同一个主机的相同进程, 如何处理 ?

# 概述和运输层服务
1. 功能: 为不同主机上运行的应用进程之间提供逻辑通信(logical communication)
    1. 发送方：把应用数据划分成 报文段(segments),交给网络层
    2. 接收方：把报文段重组成应用数据，交付给应用层
2. 端口 : 区分进程
# 多路复用与多路分解
# 无连接传输 : UD
# 可靠数据传输的原理
1. 从rdt1.0 到 rdt3.0 的变化中间,分别解决了什么问题 ? **A**
2. 画出所有FSM图像, 包括流水RS 和 GBN 的部分
3. GBN 和 RS 是如何计时的 ?
4. 
# 面向连接的传输 : TCP

# 拥塞控制原理
# TCP拥塞控制


# 问题
1. **A** 总结那些是全双工, 那些是办双工的 ?
2. 

# Transport Layer

## 3.1  Introduction and Transport-Layer Services
A transport-layer protocol provides for logical communication between application processes running on different hosts
### 3.1.1 Relationship Between Transport and Network Layers
transport -> process
network -> host
### 3.1.2 Overview of the Transport Layer in the Internet
it is less confusing to refer to both TCP and
UDP packets as segments, and reserve the term datagram for the network-layer packet.

Extending host-to-host delivery to process-to-process delivery is called transport-layer multiplexing and demultiplexing

## 3.2 Multiplexing and Demultiplexing
Each port number is a 16-bit number, ranging from 0 to 65535. The port numbers ranging from 0 to 1023 are called well-known port numbers and are restricted

### Connectionless Multiplexing and Demultiplexing
It is important to note that a UDP socket is fully identified by a two-tuple consisting of a destination IP address and a destination port number

As a consequence, if two UDP segments have different source IP addresses and/or source port numbers, but have the same destination IP address and destination port number, then the two segments will be directed to the same destination process via the same destination socket
### Connection-Oriented Multiplexing and Demultiplexing
One subtle difference between a TCP socket and a UDP socket is that a TCP socket is identified by a four-tuple: (source IP address, source port number, destination IP address, destination port number)
### Web Servers and TCP

## 3.3 Connectionless Transport: UDP
Aside from the multiplexing/demultiplexing function and some light error checking, it adds nothing to IP

with UDP there is no handshaking between sending and receiving transport-layer entities before sending a segment. For this reason,
UDP is said to be connectionless.

many applications are better suited for UDP for the following reasons:
1. Finer application-level control over what data is sent, and when.
2. No connection establishment
3. No connection state
4. Small packet header overhead

### 3.3.1 UDP Segment Structure
source port
destination port 
length
checksum

### 3.3.2 UDP Checksum

1. last addition had overflow, which was wrapped around. 
2. The 1s complement is obtained by converting all the 0s to 1s and converting all the 1s to 0
3. If no errors are introduced into the packet, then clearly the sum at the receiver will be 1111111111111111


## 3.4 Principles of Reliable Data Transfer
With a reliable channel, no transferred data bits are corrupted or lost, and all are delivered in
the order in which they were sent. This is precisely the service model offered by TCP to the Internet applications that invoke it

### 3.4.1 Building a Reliable Data Transfer Protocol


#### Reliable Data Transfer over a Perfectly Reliable Channel: rdt1.0

#### Reliable Data Transfer over a Channel with Bit Errors: rdt2.0
1. uses both positive acknowledgments and negative acknowledgments
2. In a computer network setting, reliable data transfer protocols based on such retransmissions are known as ARQ (Automatic Repeat reQuest) protocols

3. Fundamentally, three additional protocol capabilities are required in ARQ protocols to handle the presence of bit errors
    1. Error detection
    2. Receiver feedback
    3. Retransmission
    <!-- 这一个解决办法很显然在认为 ack 和 nak 的传输是 reliable 的->

4. A simple solution to unreliable transfer of ACK and NCK is to add a new field to the data packet and have the sender number its data packets by putting a sequence number into this field

5. One subtle change between rdt2.1 and rdt2.2 is that the receiver must now include the sequence number of the packet being acknowledged by an ACK message, and the sender must now check the sequence number of the packet being acknowledged by a received ACK message
    1. rdt2.1 => wait for ACK or NAK 0 
    2. rdt2.2 => wait for ACK 1
#### Reliable Data Transfer over a Lossy Channel with Bit Errors: rdt3.0
We have now assembled the key elements of a data transfer protocol. Checksums, sequence numbers, **timers**, and positive and negative acknowledgment packets each play a crucial and necessary role in the operation of the protocol

### 3.4.2 Pipelined Reliable Data Transfer Protocols
Rather than operate in a stop-and-wait manner, the sender is allowed to send multiple packets without waiting for acknowledgment

Pipelining has the following consequences for reliable data transfer protocols:
- The range of sequence numbers must be increased, since each in-transit packet (not counting retransmissions) must have a unique sequence number and there may be multiple, in-transit, unacknowledged packets.
- The sender and receiver sides of the protocols may have to buffer more than one packet. Minimally, the sender will have to buffer packets that have been transmitted but not yet acknowledged. Buffering of correctly received packets may also be needed at the receiver, as discussed below.
- The range of sequence numbers needed and the buffering requirements will depend on the manner in which a data transfer protocol responds to lost, corrupted, and overly delayed packets. Two basic approaches toward pipelined error recovery can be identified: Go-Back-N and selective repeat.


### 3.4.3 Go-Back-N (GBN)
1. 时钟的控制 base_number nextSeqNumber GBN发送的时候, 如果同时发送, 很容易出现冗余ack 的情况的, 都是解释不清楚的 ?
2. 对于time out 的处理是如何的 ?


## 3.5 Connection-Oriented Transport: TCP


TCP relies on many of the underlying principles discussed in the previous section,
including error detection, retransmissions, cumulative acknowledgments, timers,
and header fields for sequence and acknowledgment numbers. TCP is defined in
RFC 793, RFC 1122, RFC 1323, RFC 2018, and RFC 258

### 3.5.1 The TCP Connection 

. The first two segments
carry no payload, that is, no application-layer data; the third of these segments may
carry a payload

TCP is said to be connection-oriented because before one application process can
begin to send data to another, the two processes must first “handshake” with each
other—that is, they must send some preliminary segments to each other to establish the
parameters of the ensuing data transfer. 

The maximum amount of data that
can be grabbed and placed in a segment is limited by the maximum segment size
(MSS)

Note that the MSS is the maximum amount of application-layer data in the
segment, not the maximum size of the TCP segment including headers

The MSS is typically set by first determining the length of the largest
link-layer frame that can be sent by the local sending host (the so-called maximum
transmission unit, MTU)

TCP pairs each chunk of client data with a TCP header, thereby forming TCP
segments.

区分几个定义: 
1. datagram: The Internet’s network layer is responsible for moving network-layer packets known as datagrams from one host to another
2. socket:  A process sends messages into, and receives messages from, the network through a software interface called a socket
3. TCP pairs each chunk of client data with a TCP header, thereby forming TCP segments

## 3.5.2 TCP Segment Structure
1. source port 
2. destination port
3. sequence number field
4. acknowledgment number field
5. header length field (4 bit) specifies the length of the TCP header in 32-bit words. The TCP header can be of variable length due to the TCP options field
6. options field 
7. flag field 
#### Sequence Numbers and Acknowledgment Numbers
TCP’s use of
sequence numbers reflects this view in that sequence numbers are over the stream of
transmitted bytes and not over the series of transmitted segments
<!-- 为什么如何这样设置的 ? -->
The acknowledgment number that Host A puts in its segment
is the sequence number of the next byte Host A is expecting from Host B

Because TCP only acknowledges bytes up to the first missing byte in
the stream, TCP is said to provide cumulative acknowledgments

```
In truth,
both sides of a TCP connection randomly choose an initial sequence number. This is
done to minimize the possibility that a segment that is still present in the network
from an earlier, already-terminated connection between two hosts is mistaken for a
valid segment in a later connection between these same two hosts
```

##### Telnet: A Case Study for Sequence and Acknowledgment Numbers
<!-- 没有查看, 不过可以知道 sequence number 和 ack number 是没有必要相同的 -->


### 3.5.3 Round-Trip Time Estimation and Timeout


EstimatedRTT = (1 – paraA) • EstimatedRTT + paraA • SampleRTT

DevRTT = (1 – paraB) • DevRTT + paraB • | SampleRTT – EstimatedRTT |

TimeoutInterval = EstimatedRTT + 4 • DevRTT

### 3.5.4 Reliable Data Transfer
the recommended TCP timer management
procedures [RFC 6298] use only a single retransmission timer, even if there are multiple transmitted but not yet acknowledged segments

#### A Few Interesting Scenarios

#### Doubling the Timeout Interval
each time TCP retransmits, it sets the next timeout interval to twice the previous
value, rather than deriving it from the last EstimatedRTT and DevRTT

In times
of congestion, if the sources continue to retransmit packets persistently, the congestion may get worse

#### Fast Retransmit


#### Go-Back-N or Selective Repeat ?
实际上都不是的, 其实 SR是什么也是不知道啊













3.6 拥塞控制
1. 超出了网络的处理能力
2. 结果
    1. 丢包(路由器缓冲区溢出)
    2. 延时
3. 拥塞控制方法:
    1. 网络辅助的拥塞控制方法
    2. 端到端拥塞控制(由端来判断网络是否发生了拥塞)

    3. example: ATM ABR
        1. EI UI ER EFCI


4. TCP 的方法
    1. tcp 使用端到端的控制
    2. steps:
        1. 限制外发流量的速度 拥塞窗口 congestion >= lastByteSent - lastByteAck       rate = congestionWindow / RTT
        2. 感知 超时(轻度) 冗余ACK(重度)
        3. 发送发如何调节
            1.Reno
                1. 加性增 乘性减
                2. 1 MSS first, and then double
                    只要小于门限值, 采用指数增加的原则
                3. ACK timeout的策略不同
                    1. threshold 变成 1/2 采用的总是当前 w
                    2. w = 1 // w = t + 3

            2. ....
    
    3. TCP 的吞吐量
    4. TCP 的公平性
    5. TCP时间延迟建模



1. ATM 是什么 ?
2. 哪里谈过冗余ACK
3. rate 的公式的来源 ?
4. 500byte and 200ms => 200kb
5. ack 的过程
6. 初始值含有门限值吗 ?
7. 窗口移动的时候,TCP采用的重传的方式是什么 ?
8. 窗口是在滑动,还是直接翻转



1. 处理UDP的2.7.1 的编程问题
2. 