#include<iostream>

int* bubble_sort(int arr[], int length)
{
	int i, j, temp;

	for (i = 0; i < length; i++)
	{
		for (j = 0; j < length -i -1; j++)
		{
			if (arr[j] > arr[j+1])
			{
				temp = arr[j+1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	return arr;
}


int main()
{
	int arr[] = {5, 4, 3, 2, 1};
	int i, len = 5;
	int *output;

	output = bubble_sort(arr, len);
	
	for (i = 0; i < len; i++)
	{
		std::cout << output[i] << std::endl;
		std::cout << arr[i] << std::endl;
	}

	std::cout << &arr << std::endl;
	std::cout << &output << std::endl;


	return 0;
}