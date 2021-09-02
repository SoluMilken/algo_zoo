#include<iostream>

int main()
{
	int a[] = {1, 2, 3, 4, 5};
	std::cout << a << std::endl;
	std::cout << *a << std::endl;
	std::cout << a[0] << std::endl;
	std::cout << &a << std::endl;
	std::cout << sizeof(a) << std::endl;

	// std::cout << &(a+3) << std::endl;

	int *b = a;
	std::cout << b << std::endl;
	std::cout << &b << std::endl;
	std::cout << *b << std::endl;

	int i;
	for (i=0; i < 5; i++)
	{
		std::cout << b[i] << std::endl;
	}

	a[1] = 7;
	std::cout << b << std::endl;
	std::cout << b[1] << std::endl;

	// int *c = &a;  // error: cannot convert ‘int (*)[5]’ to ‘int*’ in initialization
	// std::cout << c << std::endl;
	// std::cout << *c << std::endl;
	// std::cout << **c << std::endl;

	return 0;
}
