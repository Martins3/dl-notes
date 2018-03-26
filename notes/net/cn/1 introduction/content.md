# Introduction

## 1 USES OF COMPUTER NETWORKS
Telephone calls between employees may be carried by the computer network
instead of by the phone company. This technology is called **IP telephony** or
Voice over **IP (VoIP)** when Internet technology is used. The microphone and
speaker at each end may belong to a VoIP-enabled phone or the employee’s computer. Companies find this a wonderful way to save on their telephone bills
> 似乎没有见过

<!-- 从个人的use 之后的部分的内容就是没有看的 -->

## 2 NETWORK HARDWARE
Broadly speaking, there are two types of transmission technology that are in
widespread use: broadcast links and point-to-point links.

1. Personal Area Networks e.g Bluetooth
2. Local Area Networks : wireless wifi wire Ethernet  
3. Metropolitan Area Networks : cable television networks
4. Wide Area Networks
WAN consists of *hosts* and *subnet*
In most WANs, the subnet consists of two distinct components: transmission lines and switching elements
difference from LAN: operated by different people and outers will usually connect different kinds of networking technology,  what is connected to the subnet
variance: VPN and ISP
5. Internetworks
A collection of interconnected networks is called an internetwork or internet

## 3 NETWORK SOFTWARE
1. Protocol Hierarchies
Network architectures, protocol stacks, and the protocols themselves are the principal subjects of this book

2. Design Issues for the Layers
 - Reliability
    1. routing
    2. addressing
 - network evolution:
    1. protocol layering
    2. internetworking
    3. scalable
 - resource allocation
    1. statistical multiplexing
    2. flow control
    3. congestion
 - defend threats
    1. confidentiality
    2. authentication
    3. integrity

3. Connection-Oriented Versus Connectionless Service
Layers can offer two different types of service to the layers above them: connection-oriented and connectionless
Figure 1-16

4. Service Primitives

5. The Relationship of Services to Protocols
A service is a set of primitives (operations) that
a layer provides to the layer above it.

A protocol is a set of rules governing the format and meaning of
the packets, or messages that are exchanged by the peer entities within a layer.

Entities use protocols to implement their service definitions. They are free to
change their protocols at will, provided they do not change the service visible to
their users. In this way, the service and the protocol are completely decoupled.
This is a key concept that any network designer should understand well.

An analogy with programming languages is worth making. A service is like
an abstract data type or an object in an object-oriented language. It defines operations that can be performed on an object but does not specify how these operations
are implemented. In contrast, a protocol relates to the implementation of the service and as such is not visible to the user of the service.

## 4 REFERENCE MODELS
The TCP/IP model has the opposite properties: the model itself is not of much use but the protocols are widely used
> 什么叫做model 没有用处, 而protocol 广泛使用

1. The OSI Reference Model
    1. The Physical Layer  
    2. The Data Link Layer  
        transform a raw transmission facility into a line that appears free of undetected transmission errors  
        keep a fast transmitter from drowning a slow receiver in data.
        Broadcast networks have an additional issue in the data link layer: how to control access to the shared channel 
    3. The Network Layer  
        controls the operation of the subnet
        A key design issue is determining how packets are routed from source to destination
        :confused: 不是很清楚这是为什么!
    4. The Transport Layer  
        The basic function of the transport layer is to accept data from above it, split it up into smaller units if need be, pass these to the network layer, and ensure that the pieces all arrive correctly at the other end
    5. The Session Layer  
        allows users on different machines to establish sessions between them, including dialog control, token management, synchronization
    6. The Presentation Layer  
        Unlike the lower layers, which are mostly concerned with moving bits around, the presentation layer is concerned with the syntax and semantics of the information transmitted
    7. The Application Layer  
        e.g http
    

principals: :confused: 一共含有5条,但是体会不是很深

2. The TCP/IP Reference Model
    1. The Link Layer
        permit hosts to inject packets into any network and have them travel independently to the destination (potentially on a different network)
    2. The Internet Layer
        It is designed to allow peer entities on the source and destination hosts to carry on a conversation
    3. The Transport Layer
        TCP: is a reliable connection-oriented protocol that allows a byte stream originating on one machine to be delivered without error on any other machine in the internet
        UDP:is an unreliable, connectionless protocol for applications that do not want TCP’s sequencing or flow control and wish to provide their own
    4. The Application Layer
flexible architecture

3. The Model Used in This Book
    1. Application :HTTP
    2. Transport :TCP
    3. Network :IP
    4. Link : Ethernet
    5. Physical


> 后面感觉很无聊, 以后再看, 需要代码 :confused:

