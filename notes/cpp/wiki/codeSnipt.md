
```
    int a[12];
    int *b = new int[12];
    delete[] b;

    int * beg = begin(a);
    int * ed = end(a);

    for(auto index = beg; index != ed; index ++){
        *index = 1;
    }


    for (int i : a) {
        cout << i << endl;
    }

```


```
// 反复释放 和 防卫方法
    int *b = new int[12];
    delete[] b;
    b = nullptr;

    delete[] b;

```

```
// 无符号类型
    string a = "hu bachelor";
    string::size_type  len = a.size();
    cout << len - 12 << endl;

```

```
// 使用string 的 IO
    string a = "hu bachelor";

    cin >> a;
    cout << a << endl;
    
    getline(cin, a);
    cout << a << endl;

    string a = "hu bachelor";
    a = a + "a" + "b";
    cout << a;
```

```
    vector<int> a(10);
    cout << a.size() << endl; // 数值初始化

    vector<int> b(5, 10);
    cout << b.size() << "  " << b[0] << endl;

    vector<int> c{5,10};
    cout << c.size() << "  " << c[0] << endl;

```

```
    int a[12];
    int b = 12;
    int * e = &b;
    int * &d  = e;
// 没有数组的引用
```

```
// 释放的顺序
// 析构函数 的 访问的权限也是相同
// 只有自己的函数才是需要自己单独释放的

using namespace std;
class A{
public:
    int * a;
    A(){
        a = new int;
    }

    virtual ~A(){
        delete a;
        cout << "A is released !";
    }
};

class C{
public:
    int * c;
    C(){
        c = new int[100];
    }

    ~C(){
        delete [] c;
        cout << "C is released !";
    }
};

class B : A{
    C c;

    
public:
    ~B(){
        cout << "B is released !";
    }
};
int main(){
    B b;
    return 0;
}

```


```
vector<int>  fun_five(int a){
    return {a, a, a, a};

}

int fun_six(int a){
    char c =  12;
    return  {c};
}


int main(){
    vector<int> a = fun_five(120);
    cout << a.size() << endl;
    cout << a[0] << endl;

    cout << fun_six(123);
}
```

```
前面使用 auto, 后面表示类型, 用于实现复杂类型返回值
auto fun_five(int a) -> int{
    return  a;
}
```

```
int (*fun_five())[12]{
    int c[12];
    int (*b)[12]  = &c;
    return b;
} // 返回数组指针

int * fun_six(int a[]){
    return  a;
} // 不可以返回数组, 之所以参数可以这样写, 由于在参数列表进行了转化为指针操作

```

```
// 返回函数指针

int (*fun_five(int (*a)[12]))[12]{
    int b[12];
    return &b;
}

int (* (*fun_six())(int (*)[12]))[12]{
    return fun_five;
}

```

```
// 类 内部的初始值的初始化, 仅仅可以使用 {} 和 = 来
处理
class Amazing{
    Amazing() = default;
public:
    int a;
    Amazing(int a){
        this -> a = a;
        cout << "Amazing !";
    }
};
class Blur{
public:
    Blur(){
        cout << "blur";
    }
};

class T{
public:
    Amazing amazing{11111111};
    Blur b = Blur();

};

```

```
using namespace std;

class T{
public:
    void make_amazing();
};

class Amazing{
    Amazing(){
        cout << "we can access the point !";
    }
    friend void T::make_amazing();
public:
    int a;
    Amazing(int a){
        this -> a = a;
        cout << "Amazing !";
    }
};

void T::make_amazing() {
    Amazing a;
}

```
```
// friend 的作用域

class Amazing{
    friend void func();

public:
    void what();
};

void func(){
    cout << "some function need be one friend onf Amazing !" << endl;
}

void Amazing::what() {
    func();
}



int main(){
    Amazing a;
    a.what();
}
```

```
// 类的访问权限 
#include <iostream>
#include <vector>

using namespace std;


int height = 10000;
class Amazing{
    int height = 100;
public:
    void what(int height){
        cout << height << endl;
        cout << this -> height << endl;
        cout << Amazing::height << endl;
        cout << ::height << endl;
    }
};


int main(){
    Amazing a;
    a.what(12431234);
}

```

```
// 什么J8 玩意儿 !
class A {
public:
    int a;
};

static union{
    int x = 16;
    int y = 16 * 2 + 16;
    int z = 16 * 16 * 1 + 16 * 2 + 3;
};

static union {
    int m, n;
};

int main(){
    m = 12;
}
```