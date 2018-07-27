## function
```
1. function 关键字在定义函数的时候可有可无
2. hell 函数返回值只能是整数，一般表示程序是否执行成功
3. unset .f function_name 取消函数
4. 在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...
5. $10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。

function fuckOff() {
    echo "the first is $1"
    echo "the secong is $2"
    return 1
}
fuckOff "fuck" "no fuck"
ret=$?
echo "The sum of two numbers is $ret !"
```
## 文件输入输出重定向
```
1.
命令	             说明
command > file	将输出重定向到 file。
command < file	将输入重定向到 file。
command >> file	将输出以追加的方式重定向到 file。
n > file	将文件描述符为 n 的文件重定向到 file。
n >> file	将文件描述符为 n 的文件以追加的方式重定向到 file。
n >& m	将输出文件 m 和 n 合并。
n <& m	将输入文件 m 和 n 合并。
<< tag	将开始标记 tag 和结束标记 tag 之间的内容作为输入。


 2. /dev/null 文件
如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到/dev/null：

```
## 文件包含
```
1. 使用 .filename  或者source filename
```
