#include <array>
#include <iostream>
#include <vector>
using namespace std;
void printIntArr();
int main(int argc, char const *argv[]) {
  // 标准库array
  // 内置array 不可以赋值和对象拷贝， 但是标准库可以

  // 容器大小操作
  vector<int> comp1 = {1, 2, 3, 4};
  vector<int> comp2 = {1, 2, 4};
  std::cout << (comp1 < comp2) << '\n';

  // 顺序容器操作
  // 插入元素

  printIntArr();
  return 0;
}
// 只有顺序类型才接受 大小参数，关联类型不接受

void printIntArr(){
  std::cout << " over" << '\n';
}
