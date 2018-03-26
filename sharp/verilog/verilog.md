## moudle
1. define the name  
每个端口都会连接一个信号（Signal）

申明端口的类型
input
output
inout （双向）

*Scalar and Vector*
Scalar (single bit) - 不需要给出信号的位数
input 	cin;

Vector (multiple bits) - 需要定义具体的位数
Range is MSB to LSB (left to right)
Don’t have to include zero if you don’t want to… (D[2:1])
output 	[7:0] OUT;
input 	[0:4] IN;

*how to declare the module*
module Add_half(c_out, sum, a, b);
     output sum, c_out;
     input a, b;
     …
endmodule

module Add_half(output c_out, sum,
                           input a, b);
     …
endmodule

module xor_8bit(out, a, b);
     output [7:0] out;
     input [7:0] a, b;
     …
endmodule

module xor_8bit(output [7:0] out,  input [7:0] a, b);
                          …
endmodule

2. connectivity
3.
4.
5.  functionality


## design
1. 时间延迟
  assign #2 Sum = A ^ B ; #2指2个时间单位。
   timescale 1ns / 100ps  编译指令将时间单位与物理时间关联
2. 结构描述
  使用primitive
      module mux2_1(out1,a,b,sel);
     output out1;
     input a,b,sel;

     not (sel_, sel);
     and (a1, a, sel_); // 输出在左边
     and (b1, b, sel);
     or (out1, a1, b1);
     endmodule
3. 数据流描述
    使用连续的assign,一般用于组合逻辑
4. 行为描述
  initial always 描述，组合和时序逻辑电路
  alway @( 触发条件)， 只要括号里面的东西变了，就执行begin和end之间的语句
5. 结构和行为的混合
  结构和行为描述方式可以自由混合。
  模块描述中可以包含实例化的门、模块实例化语句、连续赋值语句以及a l w a y s语句和i n i t i a l语句的混合。
  它们之间可以相互包含。

  来自always语句和i n i t i a l语句（切记只有寄存器类型数据可以在这两种语句中赋值）的值能够驱动门或开关。

  而来自于门或连续赋值语句（只能驱动线网）的值能够反过来用于触发a l w a y s语句和i n i t i a l语句。
  ```
    module FA_Mix(A,B,Cin,Sum,Cout);
    input A,B,Cin;
    output Sum,Cout;
    reg Cout;
    reg T1,T2,T3;
    wire S1;
    xor X1(S1,A,B);              //门实例语句
    always @ (A or B or Cin)   //always 语句
    begin
    T1 = A & B;
    T2 = A & Cin;
    T3 = B & Cin;
    Cout = (T1 | T2) | T3;
    end
    assign Sum = S1 ^ Cin;     //连续赋值语句
    endmodule
  ```
6.
