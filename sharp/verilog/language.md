1. 四个基础值 0  1 x z
2. 数字 <size>’<base><number>
3. Parameters & Define
4. 数据类型
  1. 线网类型。net type表示Verilog结构化元件间的物理连线。
  它的值由驱动元件的值决定；如果没有驱动元件连接到线网，线网的缺省值为z。
  ```
    wire和tri线网：是最常见的线网类型。
    wor和trior线网：如果某个驱动源为1，那么线网的值也为1。
    wand和triand线网：如果某个驱动源为0，那么线网的值为0。
    trireg线网：此线网存储数值（类似于寄存器），并且用于电容节点的建模。
    tri0和tri1线网：这类线网可用于线逻辑的建模，即线网有多于一个驱动源。
    supply0和supply1线网：supply0用于对“地”建模，即低电平0；supply1用于对电源建模，即高电平1。

  ```

  2. 寄存器类型。register type表示一个抽象的数据存储单元，它只能在always语句和initial语句中被赋值，
  并且它的值从一个赋值到另一个赋值被保存下来。寄存器类型的变量具有x的缺省值
  ```
    reg寄存器类型：是最常见的数据类型.
    integer寄存器类型：整数寄存器包含整数值，可以作为普通寄存器使用，典型应用为高层次行为建模。
    time类型：用于存储和处理时间。
    real和realtime类型：实数寄存器（或实数时间寄存器）
  ```
5. 系统任务  $ 开始的
  $display $finish $stop
  编译指令： 反引号开始的某些指令
6. delay 的类型
  1. inerial delay 类型
  2. transport delay 类型
  3. some example
    ```
    wire #5 net_1;
    delay

    and #5(a,b,c)
    ```
7. verilog 运算符
    1. vector concatenation {}
    2. reduction
8. 建模UDP
  primitive XOR（a, b, c）
  endprimitive

  然后在module 中间使用这一个
9. 阻塞赋值 和 非阻塞赋值
  1. 阻塞赋值语句（“=”）和非阻塞赋值语句（“<=”)
  2. 在assign的结构中，必须使用的是阻塞赋值
  3. 在时序逻辑电路中一般使用非阻塞赋值。
    非阻塞赋值在块结束后才完成赋值操作，此赋值方式可以避免在仿真出现冒险和竞争现象。
  4. 在组合逻辑电路中一般使用阻塞赋值。
    使用阻塞方式对一个变量进行赋值时，此变量的值在在赋值语句执行完后就立即改变。



10. synthesis 和 simulation  的书写
