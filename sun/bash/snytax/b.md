## 特殊变量

```
变量	含义
$0	当前脚本的文件名
$n	传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。
$#	传递给脚本或函数的参数个数。
$*	传递给脚本或函数的所有参数。
$@	传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同
$?	上个命令的退出状态，或函数的返回值。
$$	当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID。

echo "当前的线程号$$"
echo "当前的文件名称$0"
echo "第一个参数$1"
echo "第二个参数$2"
echo "所有的参数：$*"
echo "所有参数$@"
echo "两个特殊变量的区别："

echo "\$*=" $*
echo "\"\$*\"=" "$*"
echo "\$@=" $@
echo "\"\$@\"=" "$@"
echo "print each param from \$*"
for var in $*
do
    echo "$var"
done
echo "print each param from \$@"
for var in $@
do
    echo "$var"
done
echo "print each param from \"\$*\""
for var in "$*"
do
    echo "$var"
done
echo "print each param from \"\$@\""
for var in "$@"
do
    echo "$var"
done
```
## 转义符
```
默认是没有转义的，使用-e 可以转义，-E 禁止转义，-n 禁止插入换行符
a=10
echo "a is ${a}0\n"
echo -e "换行了\n"
echo -n "禁止换行\n"
echo -E "禁止所\t有\a的转义,但是注意\"的不是转义 "
```
## 命令替换
```
# 使用 var=`command`的语法将名命令赋值给变量
DATE=`date`
echo "DATE is $DATE"
USERS=`who | wc -l`
echo "logging user is $USERS"
UP=`date ; uptime`
echo "Uptime is $UP"
```
## 变量的替换
```
${var}	变量本来的值
${var:-word}	如果变量 var 为空或已被删除(unset)，那么返回 word，但不改变 var 的值。
${var:=word}	如果变量 var 为空或已被删除(unset)，那么返回 word，并将 var 的值设置为 word。
${var:?message}	如果变量 var 为空或已被删除(unset)，那么将消息 message 送到标准错误输出，可以用来检测变量 var 是否可以被正常赋值。
若此替换出现在Shell脚本中，那么脚本将停止运行。
${var:+word}	如果变量 var 被定义，那么返回 word，但不改变 var 的值。
```
