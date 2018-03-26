#include <iostream>
#include <vector>




class Screen{
   // friend void Window_mgr::clear(ScreenIndex);
  friend class Window_mgr;
public:
  typedef std::string::size_type pos; // public 用户才可以看见 ，也可以使用 using pos = sdt::string::size_type；

  void some_member();

  Screen(){
    std::cout << "the Screen generate funciton" << '\n';
  };

  Screen(pos ht, pos wd,char c):height(ht), width(wd), content(ht*wd, c){}

  char get() const{ //隐式内联
    return content[cursor];
  }

  inline char get(pos ht, pos wd) const;

  Screen &move(pos r, pos c);

  Screen &set(char);

  Screen &set(pos, pos, char);

  Screen &dispaly(std::ostream &os){
    do_dispaly(os);
    return *this;
  }

  const Screen &dispaly(std::ostream &os) const{
    do_dispaly(os);
    return *this;
  }

private:
  mutable size_t access_ctr; // 可变数据类型
  pos cursor = 0;
  pos height = 0,width  = 0;
  std::string content;

  void do_dispaly(std::ostream &os) const{ os << content;};
};


void Screen::some_member(){
  access_ctr++;
}

char Screen::get(pos r, pos c) const{
  pos row = r * width;
  return content[row + c ];
}

inline Screen &Screen::move(pos r, pos c){
  pos row = r * width;
  cursor = row + c;
  return *this;
}

inline Screen &Screen::set(char c){
  content[cursor] = c;
  return *this;
}

inline Screen &Screen::set(pos r, pos col, char ch){
  content[r * width + col] = ch;
  return *this;
  // 一个const 成员函数如果以引用的形式返回 *this, 那么它的返回值类型将是常量引用
}
class Window_mgr{
private:
  std::vector<Screen> screens{Screen{24, 80, ' '}};
  std::vector<int> v;
public:
  using ScreenIndex = std::vector<Screen>::size_type;
  void clear(ScreenIndex);
};

void Window_mgr::clear(ScreenIndex i){
  Screen &s = screens[i];
  s.content = std::string(s.height * s.width, ' ');
}

typedef double D;
std::string a = "out";

class A{
public:
  typedef int D;
  std::string a = "in";
  int x;
  int y;
  // 默认实参
  A(std::string l,int m = 2):x(m){
    std::cout << l << '\n';
    std::cout << x << '\n';
  }
  A(std::string info){
    std::cout << ::a << '\n'; // 输出out
    std::cout << "test the scope" << '\n';
  }

  //委托构造函数
  A(int px, int py):x(px), y(py){};
  A():A(0,0){};
  A(int s):A(s,0){};
};

class Account{
public:
  void calculate() {amount += amount * interestRate;}
  static double rate(){return interestRate;}
  static void rate(double);
private:
  std::string owner;
  double amount;
  static double interestRate; // 必须在外部初始化
  static double initRate();
};
void Account::rate(double newRate){
  interestRate = newRate;
}

double Account::interestRate = 12.0; // 初始化的时候必须添加类型的申明


// 交叉持有的形式，指针
class N;
class M{
  N* n;
};

class N{
  M m;
};

class ConsRef{
private:
  int &r;
  const int x; // 初始化的机会是通过 构造函数的的初始值列表
  ConsRef(int &k): r(k), x(k){};
};
