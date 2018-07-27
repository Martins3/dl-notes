



# Computer Network and the Internet
computer-aided manufacturing.
network’s edge and end systems 
links
switches 
access networks
physical media 

## 1.1 What Is the Internet?

### 1.1.1 A Nuts-and-Bolts Description
In Internet jargon, all of these devices are called hosts or end systems
### 1.1.2 A Services Description
### 1.1.3 What Is a Protocol ?


## 1.2 The Network Edge
end system = hosts 
### 1.2.1 Access Networks
access network—the network that physically connects an end system to the first router (also known as the “edge router”) on a path from the end system to any other distant end system.

1. Home Access: DSL, Cable, FTTH, Dial-Up, and Satellite

**DSL**(digital subscriber line):The residential telephone line carries both data and traditional telephone signals simultaneously, which are encoded at different frequencies, generally, if the residence is not located within 5 to 10 miles of the CO, the residence must resort to an alternative form of Internet access

**cable Internet access** makes use of the cable television company’s existing cable television infrastructure.Cable internet access requires special modems, called cable modems. One important characteristic of cable Internet access is that it is a shared
broadcast medium

**fiber to the home** (FTTH): There are several competing technologies for optical distribution from the CO(central office) to the homes. There are two competing optical-distribution network architectures that perform this splitting: active optical networks (AONs) and passive optical networks (PONs). AON is essentially switched Ethernet, which is discussed in Chapter 5

2. Access in the Enterprise (and the Home): Ethernet and WiFi
3. Wide-Area Wireless Access: 3G and LTE
### 1.2.2 Physical Media
1. Twisted-Pair Copper Wire
2. Coaxial Cable
3. Fiber Optics
4. Terrestrial Radio Channels  
Radio channels carry signals in the electromagnetic spectrum  
5. Satellite Radio Channels

## 1.3 The Network Core
### 1.3.1 Packet Switching
Between source and destination, each packet travels through communication links and packet switches (for which there are two predominant types, routers and link-layer switches)
1. Store-and-Forward Transmission  
a path consisting of N links each of rate R (thus, there are N-1 routers between source and destination). 
delay(end-to-end) = N * L(length) / R(rate)  
2. Queuing Delays and Packet Loss  
For each attached link, the packet switch has an output buffer (also called an output queue), which stores
packets that the router is about to send into that link  

3. Forwarding Tables and Routing Protocols  
    1. a router takes a packet arriving on one of its attached communication links and forwards that packet onto another one of its attached communication links. But how does the router determine which link it should forward the packet onto? 
    2. each router has a forwarding table that maps destination addresses (or portions of the destination addresses) to that router’s outbound links
    3. Internet has a number of special routing protocols that are used to automatically set the forwarding tables.
### 1.3.2 Circuit Switching
There are two fundamental approaches to moving data through a network of links and switches: circuit switching and packet switching  
1. Multiplexing(多路技术) in Circuit-Switched Networks  
A circuit in a link is implemented with either frequency-division multiplexing (FDM) or time-division multiplexing (TDM)  
2. Packet Switching Versus Circuit Switching
The trend has certainly been in the direction of packet switching
### 1.3.3 A Network of Networks
## 1.4 Delay, Loss, and Throughput in Packet-Switched Networks
### 1.4.1 Overview of Delay in Packet-Switched Networks
1. Types of Delay
2. Processing Delay
The time required to examine the packet’s header and determine where to direct the
packet is part of the processing delay. The processing delay can also include other
factors, such as the time needed to check for bit-level errors in the packet that occurred
in transmitting the packet’s bits from the upstream node to router A. 
3. Queuing Delay
At the queue, the packet experiences a queuing delay as it waits to be transmitted onto the link. 
4. Transmission Delay
5. Propagation Delay
6. Comparing Transmission and Propagation Delay
### 1.4.2 Queuing Delay and Packet Loss
traffic intensity approaches 1, the average queuing delay increases rapidly. A small percentage
increase in the intensity will result in a much larger percentage-wise increase in
delay
1. Packet Loss
### 1.4.3 End-to-End Delay
1. Traceroute
Because the queuing delay is varying with time, the round-trip delay of packet n sent to a router n can sometimes be longer than the round-trip delay of packet n+1 sent to router n+1  
2. End System, Application, and Other Delays
### 1.4.4 Throughput in Computer Networks
when there is no other intervening traffic, the throughput can simply be approximated as the minimum transmission rate along the path between source and destination.  
## 1.5 Protocol Layers and Their Service Models
### 1.5.1 Layered Architecture



## 问题
- 对于一个没有队列完全是空的,而且没有正在发送的link, 一个包到达此位置,那么该包是否函数有Queuing Delay
     if 10 packets arrive at an empty queue at the same time, the first packet transmitted will suffer no queuing delay,
- 什么时候会出现 bit 8 的错误  
    文件的大小的描述的时候 kb bit