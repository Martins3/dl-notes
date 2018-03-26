1. alias lm='fuckoff' 命令的别名设置
2. type  使用type 查询是外部命令还是内部命令  -t -a -p
3. tty 终端机
4. enter 紧接着反斜杠( \ ) 可以换行实现
5. echo ${PATH} 或者 echo $PATH 打印变量,{}有时可选
6. 如果一个数值没有，echo ${something_unset} 得到空行
7. 默认换行，添加\c 实现不换行
8. echo "It is a test" > result.md 将结果定向到指定的文件中间
9. chmod +x ./test.sh  #使脚本具有执行权限
```
echo $"name"
echo "name"
echo name
echo {"name"}
# 输出字符串的办法
echo "What is your name?"
read PERSON
echo "Hello, $PERSON"
```
6. 要用./test.sh告诉系统说，就在当前目录找,使用test.sh 表示的在PATH的环境中间找
7. 变量
```
注意，变量数值 变量名称都是和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。
同时，变量名的命名须遵循如下规则：
首个字符必须为字母（a-z，A-Z）。
中间不能有空格，可以使用下划线（_）。
不能使用标点符号。
不能使用bash里的关键字（可用help命令查看保留关键字）。

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。
myName= "fuck off"
readonly myName
```
8. 变量类型
```
运行shell时，会同时存在三种变量：
1) 局部变量

局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
2) 环境变量

所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3) shell变量
shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行
```
9. unset
```
myName="fuck off"
unset myName
myName="newName"
echo $myName
```
10. 使用echo可以执行命令
```
echo `date`
echo $`date`
date

但是：
echo date 的结果就是date
```
