#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[]) {
  string a = "123134";
  auto b = a.size();

  // array 不允许拷贝数组 和 使用数组的时候常常转化为指针
  // array 的维度编译的时候应该确定

  int cnt;
  std::cin >> cnt;
  int k[cnt];
  std::cout << "over" << '\n';
  for (int i = 0; i < cnt; i++) {
    k[i] = i;
  }
  for (size_t i = 0; i < cnt; i++) { //sieze_t 是一种与机器相关的无符号类型
    std::cout << k[i] << '\n';
  }
  // 不允许拷贝 和 赋值
  int sour[12] = {1, 2, 3};
  // int copy[12] = sour; 错误的

  // 数组中间可以定义指针， 但是数组不允许定义引用，否则和引用的用途相悖
  // 数组的申明
  int (* pa)[12] = &sour; // 指向数组的指针

  // 使用数组的时候，编译器会把它装化为指针

  // 指针也是迭代器

  // string 和 vector 都是可以变长的

  return 0;
}
