#include <iostream>
class Computer{
public:
  Computer()=default;

  Computer(const Computer&); // 拷贝构造函数， 如果该函数的第一个参数是自身类型的引用，而且其他的参数都有默认值

  Computer(int n){
    std::cout << "create a Computer with a number: " << n << '\n';
  } // 测试的explict关键字的使用

  Computer& operator=(const Computer&);

  void setRam(int x){Ram = x;}
  int getRam(){return Ram;}

private:
  int Ram = 0;
  int Disk = 0;
};

Computer::Computer(const Computer &orig): Ram(orig.Ram), Disk(orig.Disk){
    std::cout << "copy happened !" << '\n';
}// 合成的拷贝函数等价

Computer& Computer::operator=(const Computer& orig){
  std::cout << Ram << "copy-assignment happened" << '\n';
  Ram = 1;
  Disk = 12;
  return *this;
}
