#include <algorithm>
#include <fstream>
#include <list>
#include <iostream>
#include <vector>
#include <numeric>
#include <iterator>
#include <functional>
using namespace std;

void printVector(vector<string> &word){
  for(auto i = word.begin(); i != word.end(); ++i)
    std::cout << *i << " ";
  std::cout << "\n";
}

void printIntVec(vector<int> &word){
  for(auto i = word.begin(); i != word.end(); ++i)
    std::cout << *i << " ";
  std::cout << "\n";
}

bool isshorter(string &s1, string &s2){
    return s1.size() < s2.size();
}

bool check(const string &s, const unsigned int length){
  return s.size() > length;
}

ostream &print(const int &x, const int s,char c){
  return std::cout << x << c;
}

int main(int argc, char const *argv[]) {

  // find
  std::vector<int> v = {1, 2, 3, 4};
  auto s = find(v.begin(), v.end(), 3);
  std::cout << ((s == v.end()) ? "dis":"ok") << '\n';

  int arr[12] = {1, 2, 3, 4};
  int* arrf = find(begin(arr), end(arr), 3);
  std::cout << *arrf << '\n';

  // accumulate
  int acc= accumulate(v.cbegin(), v.cend(), -10);
  std::cout << acc << '\n';

  // equal

  //fill fill_n
  fill(v.begin(), v.end(), 1);
  std::cout << "fill " << v[1] << '\n';
  fill_n(v.begin(), v.size(), 100);
  std::cout << "fill_n " << v[v.size() - 1] << '\n';

  // back_inserter
  vector<int> em;
  auto it = back_inserter(em);
  *it = 666;
  fill_n(it, 10, 12);
  for (auto i = em.begin(); i != em.end(); ++i)
    std::cout << *i << " ";

  // copy
  int a1[] = {0, 1, 2, 3, 4, 5, 6};
  int a2[sizeof(a1)/sizeof(*a1)];
  copy(begin(a1), end(a1), a2);
  std::cout << a2 << '\n';

  // sort
  vector<string> strv = {"bs", "cdsfsdf", "aasdf", "aasdf"};
  printVector(strv);
  sort(strv.begin(), strv.end());
  printVector(strv);
  auto uni = unique(strv.begin(), strv.end());
  printVector(strv);
  strv.erase(uni, strv.end());
  printVector(strv);

  // 定制操作
  sort(strv.begin(), strv.end(), isshorter);
  printVector(strv);

  // stable_sort 相同元素位置维持不变

  // find_if 返回第一个合乎要求的元素 的迭代器

  // foreach
  for_each(strv.begin(), strv.end(), [](const string &s){std::cout << s << " ";});


  // lambda
  auto f = []{return 42;};
  std::cout << f() << '\n';
  int aa = 1,bb = 1,cv = 1;
  stable_sort(strv.begin(), strv.end(), [aa, bb, cv](const string &s1, const string &s2) mutable {return s1.size() > s2.size() + ++aa;});
  vector<int> vi = {1, -12, 34, 25,-17};
  transform(vi.begin(), vi.end(), vi.begin(), [](int i){return i > 0 ? i : -i;});
  printIntVec(vi);
  transform(vi.begin(), vi.end(), vi.begin(), [](int i) ->int {if(i > 0){return -i;} else {return i;} ;});
  printIntVec(vi);


  // bind
  auto check5 = bind(check, std::placeholders::_1, 5);
  std::cout << check5("123456") << '\n';
  int refvalue = 12;
  auto rv = bind(print, cref(refvalue), std::placeholders::_1, '\t');  // 创建ref value
  for_each(vi.begin(), vi.end(), rv);

  // iterator

  // move iterator

  // insert iterator
  list<int> st1 = {1, 2, 3, 4};
  list<int> st2, st3;
  copy(st1.cbegin(), st1.cend(), front_inserter(st2));
  copy(st1.cbegin(), st1.cend(), inserter(st3, st3.begin()));
  // stream iterator
  ifstream infile("data.md");
  istream_iterator<int> int_it(infile);
  istream_iterator<int> eof;
  vector<int> vec; // 更加使用的写法： vector<int> vec(int_it, eof)
  while(int_it!=eof){
    vec.push_back(*int_it++);
  }
  printIntVec(vec);
  // istream_iterator<int> int_it2(infile);
  // std::cout << accumulate(int_it2, eof, 0) << "cool";
  ostream_iterator<int> out_it(cout, " |");
  for(auto s:vec){
    *out_it++=s;
  }
  copy(vec.begin(), vec.end(), out_it);
  // 可以为任何定义了输入运算符的类型定义istream_iterator
  // revere iterator
  std::cout << "\nreverse iterator" << '\n';
  vector<int> rvec = {15, 72, 3, 24, 5, 66};
  for(auto a = rvec.crbegin(); a != rvec.crend(); ++a){
    std::cout << *a << ' ';
  }
  std::cout << "\nreverse sort" << '\n';
  sort(rvec.rbegin(), rvec.rend());
  printIntVec(rvec);

  //relation bwtween iterator
  string line = "what,you,are,doing";
  auto comma = find(line.begin(), line.end(), ',');
  auto lastcomma = find(line.rbegin(), line.rend(), ',');
  std::cout << string(line.begin(), comma) << '\n';
  std::cout << string(line.rbegin(), lastcomma) << '\n';
  std::cout << string(lastcomma.base(), line.end()) << '\n';

  // 泛型算法结构
  // five type iterator
  // input iterator
  // output iterator
  // bidirectional iterator
  // forward iterator
  // random-access iterator

  // 特定容器算法： list forward_list 定义了成员函数的算法
  


  return 0;
}
