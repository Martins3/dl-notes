#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

class PersonInfo{
public:
  string name;
  vector<string> phones;
};

int main(int argc, char const *argv[]) {
  ofstream outs("8H.h",ofstream::out|ofstream::trunc);
  outs.close();

  string line, word;
  vector<PersonInfo> people;
  while (getline(cin, line)) {
      PersonInfo info;
      istringstream record(line);
      record >> info.name;
      while(record >> word)
        info.phones.push_back(word);
      people.push_back(info);
  }

  return 0;
}


// 使用IO 处理string 中间的字符
// 支持宽字符对象类型
// IO对象不可以赋值 或者拷贝， 所以使用引用传递
// 当fstream对象析构的时候，close 函数自动调用
