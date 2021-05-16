#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>

int bubblesort(std::vector<int>& vec, int array_size)
{
	auto start = std::chrono::high_resolution_clock::now();
	for (int i = 0; i < array_size - 1; ++i)
	{
		for (int j = 0; j < (array_size - i - 1); ++j)
		{
			if (vec[j] > vec[j+1])
			{
				int temp = vec[j];
				vec[j] = vec[j+1];
				vec[j+1] = temp;
			}
		}
	}
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::seconds>(stop - start);

	std::ofstream myfile;
	myfile.open("results.txt", std::ios::app);
	myfile << "Time taken for Bubble sort in vector with " << array_size << " elements is: "
		<< duration.count() << " seconds" << std::endl;

	std::cout << "Time taken for Bubble sort in vector with " << array_size << " elements is: "
		<< duration.count() << " seconds" << std::endl;

	return 0;

}

int merge(std::vector<int>& vec, int first, int middle, int last)
{
	std::vector<int> leftArray(middle - first + 1);
	std::vector<int> rightArray(last - middle);

	for (unsigned int i = 0; i < leftArray.size(); ++i)
	{
		leftArray[i] = vec[first + i];
	}

	for (unsigned int j = 0; j < rightArray.size(); ++j)
	{
		rightArray[j] = vec[middle + 1 + j];
	}

	unsigned int leftIndex = 0;
	unsigned int rightIndex = 0;
	unsigned int currentIndex = first;

	while (leftIndex < leftArray.size() && rightIndex < rightArray.size()) {
		if (leftArray[leftIndex] <= rightArray[rightIndex]) {
			vec[currentIndex] = leftArray[leftIndex];
			leftIndex++;
		}
		else {
			vec[currentIndex] = rightArray[rightIndex];
			rightIndex++;
		}
		currentIndex++;
	}

	while (leftIndex < leftArray.size()) {
		vec[currentIndex] = leftArray[leftIndex];
		leftIndex++;
		currentIndex++;
	}

	while (rightIndex < rightArray.size()) {
		vec[currentIndex] = rightArray[rightIndex];
		rightIndex++;
		currentIndex++;
	}
	return 0;
}

int mergesort(std::vector<int>& vec, int first, int last, int to_print)
{
	auto start = std::chrono::high_resolution_clock::now();

	if (first >= last) {
		return 0;
	}
	int middle = (first + last) / 2;
	mergesort(vec, first, middle, to_print);
	mergesort(vec, middle + 1, last, to_print);
	merge(vec, first, middle, last);

	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::seconds>(stop - start);

	if ((first==0)&&((last+1) == to_print))
	{
	std::ofstream myfile;
	myfile.open("results.txt", std::ios::app);
	myfile << "Time taken for Merge sort in vector with " << (last + 1) << " elements is: "
		<< duration.count() << " seconds" << std::endl;

	std::cout << "Time taken for Merge sort in vector with " << (last + 1) << " elements is: "
		<< duration.count() << " seconds" << std::endl;
	}
	return 0;
}

int partitioning(std::vector<int>& vec, int first, int last)
{
	int pivot = vec[last];
	int smallestIndex = (first - 1);

	for (int i = first; i <= last - 1; ++i)
	{
		if (vec[i] < pivot)
		{
			smallestIndex++;
			int temp = vec[i];
			vec[i] = vec[smallestIndex];
			vec[smallestIndex] = temp;
		}
	}
	int temp = vec[smallestIndex+1];
	vec[smallestIndex + 1] = vec[last];
	vec[last] = temp;

	return (smallestIndex+1);
}

int quicksort(std::vector<int>& vec, int first, int last, int to_print)
{
	auto start = std::chrono::high_resolution_clock::now();
	if (first >= last)
	{
		return 0;
	}
	int partitioningIndex = partitioning(vec, first, last);
	quicksort(vec, first, partitioningIndex - 1, to_print);
	quicksort(vec, partitioningIndex + 1, last, to_print);

	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::seconds>(stop - start);

	if ((first == 0) && ((last + 1) == to_print))
	{
		std::ofstream myfile;
		myfile.open("results.txt", std::ios::app);
		myfile << "Time taken for Quick sort in vector with " << (last + 1) << " elements is: "
			<< duration.count() << " seconds" << std::endl;

		std::cout << "Time taken for Quick sort in vector with " << (last + 1) << " elements is: "
			<< duration.count() << " seconds" << std::endl;
	}
	return 0;
}


int generate(std::vector<int>& vec, int size)
{
	for (auto i = 0; i < size; ++i)
	{
		int randNumber = rand() % 4000000;
		vec.push_back(randNumber);
	}
	return 0;
}

int main()
{
	std::vector<int> ten_element_array;
	std::vector<int> hundred_element_array;
	std::vector<int> thousand_element_array;
	std::vector<int> ten_thousand_element_array;
	std::vector<int> hundred_thousand_element_array;
	std::vector<int> one_million_element_array;
	std::vector<int> four_million_element_array;

	generate(ten_element_array, 10);
	bubblesort(ten_element_array, 10);
	std::vector<int>().swap(ten_element_array);
	generate(hundred_element_array, 100);
	bubblesort(hundred_element_array, 100);
	std::vector<int>().swap(hundred_element_array);
	generate(thousand_element_array, 1000);
	bubblesort(thousand_element_array, 1000);
	std::vector<int>().swap(thousand_element_array);
	generate(ten_thousand_element_array, 10000);
	bubblesort(ten_thousand_element_array, 10000);
	std::vector<int>().swap(ten_thousand_element_array);
	generate(hundred_thousand_element_array, 100000);
	bubblesort(hundred_thousand_element_array, 100000);
	std::vector<int>().swap(hundred_thousand_element_array);
	generate(one_million_element_array, 1000000);
	bubblesort(one_million_element_array, 1000000);
	std::vector<int>().swap(one_million_element_array);
	generate(four_million_element_array, 4000000);
	bubblesort(four_million_element_array, 4000000);
	std::vector<int>().swap(four_million_element_array);
	generate(ten_element_array, 10);
	mergesort(ten_element_array, 0, static_cast<int>(ten_element_array.size() - 1), 10);
	std::vector<int>().swap(ten_element_array);
	generate(hundred_element_array, 100);
	mergesort(hundred_element_array, 0, static_cast<int>(hundred_element_array.size() - 1), 100);
	std::vector<int>().swap(hundred_element_array);
	generate(thousand_element_array, 1000);
	mergesort(thousand_element_array, 0, static_cast<int>(thousand_element_array.size() - 1), 1000);
	std::vector<int>().swap(thousand_element_array);
	generate(ten_thousand_element_array, 10000);
	mergesort(ten_thousand_element_array, 0, static_cast<int>(ten_thousand_element_array.size() - 1), 10000);
	std::vector<int>().swap(ten_thousand_element_array);
	generate(hundred_thousand_element_array, 100000);
	mergesort(hundred_thousand_element_array, 0, static_cast<int>(hundred_thousand_element_array.size() - 1), 100000);
	std::vector<int>().swap(hundred_thousand_element_array);
	generate(one_million_element_array, 1000000);
	mergesort(one_million_element_array, 0, static_cast<int>(one_million_element_array.size() - 1), 1000000);
	std::vector<int>().swap(one_million_element_array);
	generate(four_million_element_array, 4000000);
	mergesort(four_million_element_array, 0, static_cast<int>(four_million_element_array.size() - 1), 4000000);
	std::vector<int>().swap(four_million_element_array);
	generate(ten_element_array, 10);
	quicksort(ten_element_array, 0, static_cast<int>(ten_element_array.size() - 1), 10);
	std::vector<int>().swap(ten_element_array);
	generate(hundred_element_array, 100);
	quicksort(hundred_element_array, 0, static_cast<int>(hundred_element_array.size() - 1), 100);
	std::vector<int>().swap(hundred_element_array);
	generate(thousand_element_array, 1000);
	quicksort(thousand_element_array, 0, static_cast<int>(thousand_element_array.size() - 1), 1000);
	std::vector<int>().swap(thousand_element_array);
	generate(ten_thousand_element_array, 10000);
	quicksort(ten_thousand_element_array, 0, static_cast<int>(ten_thousand_element_array.size() - 1), 10000);
	std::vector<int>().swap(ten_thousand_element_array);
	generate(hundred_thousand_element_array, 100000);
	quicksort(hundred_thousand_element_array, 0, static_cast<int>(hundred_thousand_element_array.size() - 1), 100000);
	std::vector<int>().swap(hundred_thousand_element_array);
	generate(one_million_element_array, 1000000);
	quicksort(one_million_element_array, 0, static_cast<int>(one_million_element_array.size() - 1), 1000000);
	std::vector<int>().swap(one_million_element_array);
	generate(four_million_element_array, 4000000);
	quicksort(four_million_element_array, 0, static_cast<int>(four_million_element_array.size() - 1), 4000000);
	std::vector<int>().swap(four_million_element_array);

	/*
	for (std::vector<int>::iterator it = ten_element_array.begin(); it != ten_element_array.end(); it++)
	std::cout << *it << " ";
	*/

	return 0;
	
}

