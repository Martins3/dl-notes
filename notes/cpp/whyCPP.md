1. std::cout<< "" << std::endl 和 std::cout << "" << "\n" 有没有什么区别
2.
```
int const m2 = i2;
const int m3 = i2;
有没有区别 ？  
```
3. 101 warning  内置类型
4. array 的维度必须是常量表达式的说法测试显示的结果不是如此的
6. 定义在类内部的 inline 函数 和定义在类外部的函数的 有什么区别 ？
7. 如何理解对象指针 ？
8. 类的 成员函数 类相关的非成员函数 的放置的位置在什么地方 ？
9. 内置类型
10. 242 友元的申明 不是很清楚想要表达的内容 ？ ; 友元是否可以访问权限必定为了解决private 的,为什么P543的 diction 那就是有问题的 !
11. 246 类内初始值
12. 252 类的申明的依赖问题
13. 类的作用域的说法测试不是如此， 253
14. 默认构造函数，谁会被选定为默认的构造函数
15. 262 块作用域 等等难以体会 直接到达静态类 =>
16. 字面值常亮类型 contsexper
17. 不完全类型
18. explicit 构造函数 265
19. 标准库array 和 直接使用的array 有什么区别 ？
20. array<int, 20>::size_type j; 中间的size_type 是做什么的 ？
21. 函数指针
22. 默认参数
23. 357 bind的ref ，既然原先的函数申明的时候就是 使用的为  ostream & ,那么为什么 再次使用ref 来防止拷贝 ，bind 和普通的函数为什么在此处含有区别
24. 头文件的使用 ，如果在 H1.cpp 中间 include iostream，然后又在 H1.h  中间引用 iostream ，得到的结果是什么 ？
25. 聚合类 266
26. A copy constructor is a constructor which first parameter is a reference to the class type and any additional parameters have default values. 也就是说copy constructor 的参数列表的数值不仅仅只有一个，其他的参数含有的默认值是什么意思？
27. new 运算符的使用的含义是什么？
28. Computer a* = new Computer; 和  Computer* a = new Computer(); 有什么区别 ？
29. 迭代器适配器
30. 359 那些类型没有定义输入运算符，为什么没有定义，他们具有什么特点？
31. 解引用运算符 *
32. 模板类 的 定义
33. 302 9.2.5 测试的结果和想象不一致，书上的说法也显得比较混乱
34. 总结引用
35. 再问一次: 为什么会有头文件, 如何使用头文件, 为什么java 和 Python 都没有头文件的 ?
36. string& a() const{// todo} 中间的const 是用于干什么的啊！ 
37. extern 的使用原则
38. P543 protected 的 保护的第三条规则 !
39. 局部static 对象 185 类static 对象 268
40. C 的 static 如何使用, C++ 的 class 的 static 如何使用, 如果 C++对于C 的 static 是兼容的, 不会产生冲突吗 ?
41. 什么是 伴随类 弱引用
42. auto 如何使用 ? C 中间的auto 是如何的使用的. C++ 中间的 auto 的如何推断的类型的, 有什么的顾忌的
43. P89 直接初始化 : 解释 值初始化的理由不是很清楚
44. https://stackoverflow.com/questions/184537/in-what-cases-do-i-use-malloc-vs-new

1. java 的interface 在其他的语言的体现在于何处 ?
2. 多继承 带来那些好处, 同时带来了那些问题 ?
3. java的 class 上面是携带 访问权限控制的, 那么C++ 对应的位置的 作用体现于 何处 ?
4. 如何理解 类的用户 ?
5. 为什么 java 没有 友元
6. 友元 为了 编写者 而创建的, 那么继承是给 编写者 还是 用户, 还是都有, 如果都有, 如何区分对待两种 人 ?
7. 封装 具体表示为什么: 用户没有办法查看的源代码, 还是说用户没有必要暴露在 开发者 的复杂之下, 如果是第二者的话, 为什么不是warning ,而是error 的 ?
8. 总结静态内存 和 栈内存
9. 为什么 C++ 中间不可以在函数中间添加的函数 ?
10. smart pointer , java 在 C++ 的那些基础上面消除了 pointer, java 的那些做法是对应这 smart pointer  ! 
11. 表达式的类型如何处理 ?

1. 头文件
    1. 头文件为了解决什么问题而产生的 ?
    2. 头文件的操作规则是什么 ?
        1. include 之后, 然后使用文件中间的内容对于include 进行替换, 是不是 ?
        2. 那么 java 的 import 和这 有什么区别
        3. 是不是可以推测, 一个正常的工程中间几乎全部都是 .h文件的(类似java只有 main 文件含有 main 函数一样)
        4. 为什么C++的 include 非要自己手写
    3. 


