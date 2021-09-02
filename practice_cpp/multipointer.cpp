#include<iostream>

bool new_int_array(int nCount, int** ppRet)
{
	int* pData = new int[nCount];
	int i;
	for (i=0; i < nCount; i++)
	{
		pData[i] = i;
		// std::cout << pData[i] << std::endl;
	}
	// std::cout << pData << std::endl;
	std::cout << ppRet << std::endl;
	std::cout << *ppRet << std::endl;
	if (pData == NULL){
		*ppRet = NULL;
		return false; 
	}
	else{
		*ppRet = pData;
		std::cout << ppRet << std::endl;
		std::cout << *ppRet << std::endl;
		std::cout << (*ppRet)[2] << std::endl;
		return true;
	}
}


int main()
{
	bool output;
	int i, b = 3;
	int*bb = new int[b];
	int** aa = &bb;
	output = new_int_array(b, aa);
	// std::cout << output << std::endl;
	// std::cout << aa << std::endl;
	// std::cout << *aa << std::endl;
	for (i=0; i < b; i++)
	{
		std::cout << (*aa)[i] << std::endl;
	}
	// std::cout << **aa[1] << std::endl; 
	return 0;
}