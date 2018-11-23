#include "H6.h"
#include <iostream>
#include <typeinfo>
void reset(int &i){ // ref 传入的参数可以是 ref 或者 int
  i = 1;
}
int main(int argc, char const *argv[]) {
  int n = 0;
  int &r = n;
  bool x = false;
  std::cout << typeid(r).name() << '\n';
  std::cout << typeid(x).name() << '\n';

  //顶层const and ref
  const int ci = 42;
  int i = ci; //i 不会持有const
  int &j = i;
  int * const pi = &i; // pointer is const
  *pi = 12; // use the pointer to change i
  const int &cr = 12; // 常量引用可以实现对于字面量赋值
  reset(j);
  std::cout << i << '\n';

  // 

  return 0;
}
