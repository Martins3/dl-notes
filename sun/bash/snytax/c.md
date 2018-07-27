## 运算符
```
1. 乘法需要借助\
2. 没有内置的数学计算，需要使用 expr或者awk
3. 表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2

a=10
b=20
运算符	    说明	        举例
+	加法	`expr $a + $b`   结果为 30。
-	减法	`expr $a - $b`   结果为 10。
*	乘法	`expr $a \* $b`  结果为  200。
/	除法	`expr $b / $a`   结果为 2。
%	取余	`expr $b % $a`   结果为 0。
=	赋值	a=$b 将把变量 b   的值赋给 a。
==	相等。用于比较两个数字，相同则返回 true。	[ $a == $b ] 返回 false。
!=	不相等。用于比较两个数字，不相同则返回 true。	[ $a != $b ] 返回 true。
```
## 比较运算符
```
EQ 就是 EQUAL等于
NQ 就是 NOT EQUAL不等于
GT 就是 GREATER THAN大于　
LT 就是 LESS THAN小于
GE 就是 GREATER THAN OR EQUAL 大于等于
LE 就是 LESS THAN OR EQUAL 小于等于
```
## 布尔运算
```
!	非运算
-o	或运算
-a	与运算
```
## String处理
```
运算符	说明	举例
=	检测两个字符串是否相等，相等返回 true。	[ $a = $b ] 返回 false。
!=	检测两个字符串是否相等，不相等返回 true。	[ $a != $b ] 返回 true。
-z	检测字符串长度是否为0，为0返回 true。	[ -z $a ] 返回 false。
-n	检测字符串长度是否为0，不为0返回 true。	[ -z $a ] 返回 true。
str	检测字符串是否为空，不为空返回 true。	[ $a ] 返回 true。

a="abc"
b="def"
c=""
if [[ $a = $b ]]; then
    echo "a and b is same"
else
    echo "a and b is not same"
fi

if [[ c ]]; then
    echo "c is not empty"
else
    echo "c is empty"
fi
```
## 文件测试运算符
```
操作符	说明	举例
-b file	是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
-c file	是否是字符设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
-d file	是否是目录，如果是，则返回 true。	[ -d $file ] 返回 false。
-f file	是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
-g file	是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
-k file	是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
-p file	是否是具名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
-u file	是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
-r file	是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
-w file	是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
-x file	是否可执行，如果是，则返回 true。	[ -x $file ] 返回 true。
-s file	是否为空（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
-e file	（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true

```
