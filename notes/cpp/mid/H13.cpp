#include <iostream>
#include "H13.h"
int main(int argc, char const *argv[]) {
  Computer* f = new Computer(12);
  Computer s = *f;
  Computer a;
  a.setRam(100);
  Computer b;
  b.setRam(10000000);
  a = b;
  std::cout << a.getRam() << '\n';
  // 重载运算符 的 使用

  return 0;
}
// copy constructure
// copy-assignment constructure
// move constructure
// move-assignment constructure
// destructor
