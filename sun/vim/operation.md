i → Insert 模式，按 ESC 回到 Normal 模式.
x → 删当前光标所在的一个字符。
wq → 存盘 + 退出 (:w 存盘, :q 退出)   （陈皓注：:w 后可以跟文件名）
dd → 删除当前行，并把删除的行存到剪贴板里
p → 粘贴剪贴板

a → 在光标后插入
o → 在当前行后插入一个新行
O → 在当前行前插入一个新行
cw → 替换从光标所在位置后到一个单词结尾的字符地插入

0 → 数字零，到行头
^ → 到本行第一个不是blank字符的位置（所谓blank字符就是空格，tab，换行，回车等）
$ → 到本行行尾
g_ → 到本行最后一个不是blank字符的位置。
/pattern → 搜索 pattern 的字符串（陈皓注：如果搜索出多个匹配，可按n键到下一个）

P/p → 粘贴 p 表示当前的位置的粘贴，P表示之后的位置粘贴
yy → 拷贝当前行当行于 ddP

u → undo
<C-r> → redo

:e <path/to/file> → 打开一个文件
:w → 存盘
:saveas <path/to/file> → 另存为 <path/to/file>
:x， ZZ 或 :wq → 保存并退出 (:x 表示仅在需要时保存，ZZ不需要输入冒号并回车)
:q! → 退出不保存 :qa! 强行退出所有的正在编辑的文件，就算别的文件有更改。
:bn 和 :bp → 你可以同时打开很多文件，使用这两个命令来切换下一个或上一个文件。（陈皓注：我喜欢使用:n到下一个文件）

# visual mood
1. v hjjjklh d
2. V linewise
3. <c-v> blockwise

# text object
1. use in the visual mood or  Operator-pending mode
2. aw as ap
3. Some text objects are similar to some *motion* s

# numerb
1. Insert the same words: number+ i + content + ESC

# comment code and uncomment code
1. ESC
2. <c-v>
3. I(shift i)
4. type what you want
5. ESC
# 搜索
1. 不区分大小写的搜索：
2. 

# 操作多个文件
