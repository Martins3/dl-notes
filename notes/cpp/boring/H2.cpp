#include <iostream>
using namespace std;
int main(int argc, char const *argv[]) {
  //auto
  int i = 0, &r =i;

  // top-level const low-level const
  // 就指针而言： 顶层表示为指针 ，底层表示指向的数值，就其他而言：顶层表示自己 ；
  // 底层： 变量可以转化为常量，反之不可以, 原因是描述了该可以通过该指针修改指向的数值
  // ref 全部都是底层指针
  //
  int i2 = 1;
  int const m2 = i2;
  const int n2 = i2;
  int s2 =  n2;
  const int *  p2 = &m2;
  const int * pa2 = &i2;

  // compound type
  // ref 必须被初始化 int & a;
  // ref 必须和对象关联 不可以使用数值或者是表达式
  int i3 = 1;
  int j3 = 2;
  int &a3 = i3;
  a3 = j3;

  // 复合类型
  

  return 0;
}
