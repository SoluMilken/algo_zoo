#include <iostream>


int main()
{
    std::cout << "start" << std::endl;
    const int a = 1;
    std::cout << a << std::endl;
    std::cout << &a << std::endl;
    // a = 100; -> a is read-only -> compile error

    const int *b = &a;
    std::cout << b << std::endl;
    std::cout << *b << std::endl;
    return 0;
}
