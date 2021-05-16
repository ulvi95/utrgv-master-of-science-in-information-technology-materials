#include <iostream>
#include <vector>
#include <algorithm>

void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

int Partition(int array_to_find[], int l, int r)
{
	int last = array_to_find[r], i = l, j = l;
	while (j < r) {
		if (array_to_find[j] < last)
		{
			swap(&array_to_find[i], &array_to_find[j]);
			i++;
		}
		j++;
	}
	swap(&array_to_find[i], &array_to_find[r]);
	return i;
}

int randomPartition(int array_to_find[], int l, int r)
{
	int n = r - l + 1;
	int pivot = std::rand() % n;
	swap(&array_to_find[l + pivot], &array_to_find[r]);
	return Partition(array_to_find, l, r);
}

void MedianUtil(int array_to_find[], int l, int r, int k, int& a, int& b)
{
	if (l <= r) {
		int partitionIndex = randomPartition(array_to_find, l, r);
		if (partitionIndex == k) {
			b = array_to_find[partitionIndex];
			if (a != -1)
				return;
		}
		else if (partitionIndex == k - 1) {
			a = array_to_find[partitionIndex];
			if (b != -1)
				return;
		}
		if (partitionIndex >= k)
			return MedianUtil(array_to_find, l, partitionIndex - 1, k, a, b);
		else
			return MedianUtil(array_to_find, partitionIndex + 1, r, k, a, b);
	}
	return;
}

int findMedian(int array_to_find[], int n)
{
	int median_result, a = -1, b = -1;
	if (n % 2 == 1) {
		MedianUtil(array_to_find, 0, n - 1,
			n / 2, a, b);
		median_result = b;
	}
	else {
		MedianUtil(array_to_find, 0, n - 1,
			n / 2, a, b);
		median_result = (a + b) / 2;
	}
	return median_result;
}

int main()
{
	int array_to_find[] = { 1,1,1,1,1,1,2,2,2,2,2,2 };
	int n = sizeof(array_to_find) / sizeof(array_to_find[0]);
	int median = findMedian(array_to_find, n);
	int counter = 0;
	for (int i = 0; i < n; i++)
	{
		if (array_to_find[i] == median)
		{
			counter++;
		}
	}
	if (counter > (n / 2))
	{
		std::cout << "Majority element is equal to " << median;
	}
	else
	{
		std::cout << "There is no majority element " << std::endl;
	}
	return 0;
}

