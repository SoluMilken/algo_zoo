#include<iostream>

using namespace std;


class Base
{
private:

	int private_attr;
	void show_private()
	{
		cout << "private attr is " << private_attr << endl;
	};

protected:
	int protected_attr;
	int show_protected()
	{
		cout << "protected attr is " << protected_attr << endl;
	};

public:
	// Base(): public_attr(3)
	// {} 
	// private_attr(1), protected_attr(2)
	Base(){
		public_attr = 3;
		cout << "[init] default" << endl;
	}
	Base(int p)
	{
		public_attr = p;
		cout << "[init] assigned attr " << public_attr << endl;
	}
	int public_attr;
	void show_public()
	{
		cout << "[show] " << public_attr << endl;
		// cout << "public attr is";
		// return 0;
	};
};




int main()
{
	Base b = Base();
	Base c = Base(3);
	b.show_public();
	return 0;
	// b = Base(1, 2, 3)
}