#include <iostream>
#include <typeinfo>
int main(int argc, char *argv[])
{
    std::cout << "fuck you" << std::endl;
    std::cerr << "cerr message" << '\n';
    std::clog << "clog message" << '\n';

    

    void*( *const(* Hama(const int * a, double(*(*const b)[8])(int))  )  [16][32])   (const int* const);
    // double(*(*const)[8])(int)
    void (* Hama2(int) )  (int);

    void(*(* DaHama(int))[3]) (int);

    double(*(b)[8])(int);

    std::cout << typeid(Hama).name() << '\n';
    return 0;
}
