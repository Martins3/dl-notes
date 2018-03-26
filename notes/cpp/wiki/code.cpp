#include <iostream>
using namespace std;
class A{
public:
protected:
    int a;
};

class B : private A{
public:
   using A::a;
};
int main(){
    B b;
    cout << b.a;
}
