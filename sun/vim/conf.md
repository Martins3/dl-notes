# 配置文件原则


# 资源
[github repo](https://github.com/spf13/spf13-vim)
[the holy shit](https://github.com/spf13/spf13-vim) curl https://j.mp/spf13-vim3 -L -o - | sh
https://github.com/amix/vimrc(some key map)
https://github.com/wklken/k-vim(this is far more interesting and I think this seems to be the final one)
https://github.com/vim-scripts/Solarized(a theme)
https://github.com/tpope/vim-pathogen(install bundle)

# theme
1. how to change the theme https://github.com/wklken/k-vim/wiki
2. what is the best theme
3. 如何修改字体的粗细


# bundle
1. what is the best bundles

## nerdTree 
1. 配置打开的快捷键

2. 窗口： ctrl +（hjkl)
3. tab : 不是同时的使用gt,而是连续的使用gt
4. 调节nerd tree 的宽度 ctrl shift w < (简直有病，有事连续而不是同时)  
5. 设置字体 首先查找frontsize,然后修改原始部分代码，不可以直接按照stackoverflow 上面
> http://kennedysgarage.com/articles/nerdtree/


由于使用的为k-vim 它自动的设置了很多快捷键：
注意, 以下 ',' 代表<leader>
4. 上排F功能键
F1 废弃这个键,防止调出系统帮助
F2 set nu/nonu,行号开关，用于鼠标复制代码用
F3 set list/nolist,显示可打印字符开关
F4 set wrap/nowrap,换行开关
F5 set paste/nopaste,粘贴模式paste_mode开关,用于有格式的代码粘贴
F6 syntax on/off,语法开关，关闭语法可以加快大文件的展示

F9 tagbar
F10 运行当前文件(quickrun)

5. 分屏移动

ctrl + j/k/h/l   进行上下左右窗口跳转,不需要ctrl+w+jkhl

6. 搜索
<space> 空格，进入搜索状态
/       同上
,/      去除匹配高亮

(交换了#/* 号键功能, 更符合直觉, 其实是离左手更近)
#       正向查找光标下的词
*       反向查找光标下的词

优化搜索保证结果在屏幕中间

7. tab操作
ctrl+t 新建一个tab

(hjkl)
,th    切第1个tab
,tl    切最后一个tab
,tj    下一个tab
,tk    前一个tab

,tn    下一个tab(next)
,tp    前一个tab(previous)

,td    关闭tab
,te    tabedit
,tm    tabm

,1     切第1个tab
,2     切第2个tab
...
,9     切第9个tab
,0     切最后一个tab

,tt 最近使用两个tab之间切换
(可修改配置位 ctrl+o,  但是ctrl+o/i为系统光标相关快捷键, 故不采用)

8. buffer操作(不建议, 建议使用ctrlspace插件来操作)
[b    前一个buffer
]b    后一个buffer
<-    前一个buffer
->    后一个buffer


9. 按键修改
Y         =y$   复制到行尾
U         =Ctrl-r
,sa       select all,全选
,v        选中段落
kj        代替<Esc>，不用到角落去按esc了

,q     :q，退出vim
,w     :w, 保存当前文件

ctrl+n    相对/绝对行号切换
<enter>   normal模式下回车选中当前项

更多细节优化:
    1. j/k 对于换行展示移动更友好
    2. HL 修改成 ^$, 更方便在同行移动
    3. ; 修改成 : ，一键进入命令行模式，不需要按shift
    4. 命令行模式 ctrl+a/e 到开始结尾
    5. <和> 代码缩进后自动再次选中, 方便连续多次缩进, esc退出
    6. 对py文件，保存自动去行尾空白，打开自动加行首代码
    7. 'w!!'强制保存, 即使readonly
    8. 去掉错误输入提示
    9. 交换\`和', '能跳转到准确行列位置
    10. python/ruby 等, 保存时自动去行尾空白
    11. 统一所有分屏打开的操作位v/s[nerdtree/ctrlspace] (特殊ctrlp ctrl+v/x)
    12. ',zz' 代码折叠toggle
    13. python使用"""添加docstring会自动补全三引号
    14. Python使用#进行注释时, 自动缩进
