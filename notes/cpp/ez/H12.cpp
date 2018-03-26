#include<iostream>
#include<memory>
#include<string>
#include<vector>
using namespace std;

void one(){
    shared_ptr<int> p3 = make_shared<int>(42);
    cout << *p3;
}

int main(){
    one();
    vector<int> a(10);
    
}