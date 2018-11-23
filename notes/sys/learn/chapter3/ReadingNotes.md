

---
## AT&T assembly
1. All of the lines beginning with ‘.’ are directives to guide the assembler and
linker

We see that the Intel and ATT formats differ in the following ways:
- The Intel code omits the size designation suffixes. We see instruction mov instead of movl.
- The Intel code omits the ‘%’ character in front of register names, using esp instead of %esp.
- The Intel code has a different way of describing locations in memory, for example ‘DWORD PTR
[ebp+8]’ rather than ‘8(%ebp)’.
- Instructions with multiple operands list them in the reverse order. This can be very confusing when
switching between the two formats.


## GCC 使用
gcc -01 -o p a.c b.c   

对于全部的流程:
gcc -E code.c -o code.i #预处理  
gcc -S code.i -o code.s #编译  
gcc -C code.s -o code.o # 生成可重定向的代码  
gcc code.c -o code  
上面的三条的仅仅是展示编译的过程,可以使用gcc 可以直接编译为code.o 使用 -C 参数
说明一下关于命令行参数的使用的原则,由于使用了-o 之类的东西,所以没有必要强调顺序的  
从code.o 得到code 使用的是link
当然也是可以使用: gcc -O1 -o prog code.o main.c

-01 优化的级别  


gcc -o1 -S -masm=intel sum.c  获取intel 格式的汇编代码

使用objdump -d code.o 和 objdump -o code 可以查看对于可重定向的不可重定向的区别
## 杂记
[hyper threading](https://en.wikipedia.org/wiki/Hyper-threading)
