#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

static bool cmp(const vector<int>& a,const vector<int>& b) {
	// cout << a[0] << " " << b[0] << endl;
    if (a[0] == b[0])
    {
    	return a[1] < b[1];
    }
   	return a[0] < b[0];
}

int main()
{
	vector< vector<int> > vec;
	vector<int> sub_v1;
	// vector<int>::iterator it_i;
	vector<int> sub_v2;
	vector <int> sub_v3;
	
	sub_v1.push_back(3);
	sub_v1.push_back(10);
	sub_v2.push_back(3);
	sub_v2.push_back(7);
	sub_v3.push_back(1);
	sub_v3.push_back(2);
	vec.push_back(sub_v1);
	vec.push_back(sub_v2);
	vec.push_back(sub_v3);

	sort(vec.begin(), vec.end(), cmp);
	
	for (int i = 0; i < vec.size(); i++)
	{
		cout << vec[i] << endl;
		cout << vec[i][0] << " " << vec[i][1] << endl; 	
	}
	// for(it_i=vec.begin(); it_i!=vec.end(); ++it_i)
	// {
	// // 	cout << it_i << " "; 
	// 	cout << *it_i << " "; 		
	// }
	// } cout << *it_i << " "; 
	// cout << sub_v1.begin() << endl; 
	return 0;
}