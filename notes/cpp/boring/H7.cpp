#include <iostream>
#include "H7.h"
class Sales_data{
  friend Sales_data add(const Sales_data&, const Sales_data&);
  friend std::ostream &print(std::ostream&, const Sales_data&);
  friend std::istream &read(std::istream&, Sales_data&);
public:
  // 构造函数
  Sales_data() = default;
  Sales_data(const std::string &s): bookNo(s){}
  Sales_data(const std::string &s, unsigned n, double p): bookNo(s), units_sold(n), revenue(p*n){}
  Sales_data(std::istream &);

  // 成员函数
  std::string isbn() const {return bookNo;}
  Sales_data& combine(const Sales_data&);
private:
  double avg_price() const;
  std::string bookNo;
  unsigned units_sold = 0;
  double revenue = 0.0;
};

double Sales_data::avg_price() const {
  if (units_sold){
    return revenue / units_sold;
  }else{
    return 0;
  }
}

Sales_data& Sales_data::combine(const Sales_data &rhs){
  units_sold += rhs.units_sold;
  revenue += rhs.revenue;
  return *this;
}

// 与类相关非成员函数
Sales_data add(const Sales_data&, const Sales_data&);
std::ostream &print(std::ostream&, const Sales_data&);
std::istream &read(std::istream&, Sales_data&);

std::istream &read(std::istream &is, Sales_data &item){
  double price = 0;
  is >> item.bookNo >> item.units_sold >> price;
  item.revenue = price * item.units_sold;
  std::cout << "finish !" << '\n';
  return is;
}

std::ostream &print(std::ostream &os, const Sales_data &item){
  os << item.isbn() << " " <<  item.units_sold << " " << item.revenue << " "
     << item.avg_price();
  return os;
}

Sales_data add (const Sales_data &lhs, const Sales_data &rhs){
  Sales_data sum = lhs;
  sum.combine(rhs);
  return sum;
}

Sales_data::Sales_data(std::istream &is){
  read(is, *this); //  函数的顺序很重要的
}





// 所有的成员都必须在类中间申明，但是只有定义无所谓, 申明了，那么就是一定要定义在外面的位置 ！
// const 函数， 修改this 指针类型
// 类拷贝 赋值 析构




int main(int argc, char const *argv[]) {
  /* code */
  std::cout << "happy" << '\n';
  Screen s;
  A aa("wow, like python", 12);


  return 0;
}
