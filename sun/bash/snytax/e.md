## printf
```
1. printf 命令不用加括号
2. format-string 可以没有引号，但最好加上，单引号双引号均可。
3. 参数多于格式控制符(%)时，format-string 可以重用，可以将所有参数都转换。
4. arguments 使用空格分隔，不用逗号。
5. %d 参数错误或者没有参数，显示0 %s 显示NULL

printf %s%d abc 4
printf "%s %s %s\n" a b c d e f g h i j
printf "The first program always prints'%s,%d\n'" Hello Shell
```
## if
```
1. 经常和test 连用
2. 可以写在一行

num1=$1
num2=$2
if test $[num1] -gt $[num2]
then
    echo 'num1 is greater than num2!'
elif [[ $num1 -eq $num2 ]]; then
    echo 'The two numbers are equal!'
else
    echo "num1 is smaller than num2!"
fi
```
## case
```
1. ;; 与其他语言中的 break 类似，一旦匹配跳过所有的可能,但是这是必须添加的内容
2. 如果无一匹配模式，使用星号 * 表示对于所有的可能结果的匹配。

aNum=3
case $aNum in
    1)  echo 'You select 1';;
    2)  echo 'You select 2';;
    3)  echo 'You select 3';;
    4)  echo 'You select 4';;
    *)  echo 'You do not select a number between 1 to 4';;
esac
```
## for loop
```
1. 列表是一组值（数字、字符串等）组成的序列，每个值通过空格分隔。
2. 每循环一次，就将列表中的下一个值赋给变量。

for FILE in $HOME/.bash*
do
   echo $FILE
done
```
## while
```
echo 'type <CTRL-D> to terminate'
echo -n 'enter your most liked film: '
while read FILM
do
    echo "Yeah! great film the $FILM"
done
```
## until
```
until command
do
   Statement(s) to be executed until command is true
done
```
## break cotinue
```
 在嵌套循环中，break 命令后面还可以跟一个整数，表示跳出第几层循环。
 echo "input 100 to stop the game"
 while :
 do
     echo -n "Input a number between 1 to 5: "
     read aNum
     case $aNum in
         1|2|3|4|5) echo "Your number is $aNum!"
         ;;
         *) echo "You do not select a number between 1 to 5!"
         if [[ $aNum == 100 ]]; then
             echo "Game is over!"
             break
         fi
         echo "the number is out of range"
             continue
             echo "this line can never be executed"
         ;;
     esac
 done

```
