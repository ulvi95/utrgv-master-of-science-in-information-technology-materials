
#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <string>

bool** check_vector;
std::ofstream myfile;

std::string str = "";

void printing_available_subsets(int a[], int i, int s, std::vector<int>& p)
{

	if (i == 0 && s != 0 && check_vector[0][s])
	{
		p.push_back(a[i]);
		if (a[i] == s)
		{
			for (int i = 0; i < p.size(); ++i)
			{
				printf("%d ", p[i]);
				str += std::to_string(p[i]);
				str += " ";
			}
			printf("\n");
			str += "\n";
		}
		return;
	}

	// If s becomes 0
	if (i == 0 && s == 0)
	{
		for (int i = 0; i < p.size(); ++i)
		{
			printf("%d ", p[i]);
			str += std::to_string(p[i]);
			str += " ";
		}
		printf("\n");
		str += "\n";
		return;
	}

	// If given s can be achieved after ignoring
	// current element.
	if (check_vector[i - 1][s])
	{
		// Create a new vector to store path
		std::vector<int> b = p;
		printing_available_subsets(a, i - 1, s, b);
	}

	// If given s can be achieved after considering
	// current element.
	if (s >= a[i] && check_vector[i - 1][s - a[i]])
	{
		p.push_back(a[i]);
		printing_available_subsets(a, i - 1, s - a[i], p);
	}
}

//int knapsack(std::vector<int> a, int n, int s, std::vector<int>& subset, int size_of_subset)
int knapsack(int a[], int n, int s, std::vector<int>& subset)
{
	if (n == 0 || s < 0)
		return 0;
	check_vector=new bool* [n];
	for (int i = 0; i < n; ++i)
	{
		check_vector[i] = new bool[s + 1];
		check_vector[i][0] = true;
	}

	if (a[0] <= s)
		check_vector[0][a[0]] = true;
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < s+1; j++)
		{
			if (a[i] > j)
			{
				check_vector[i][j] = check_vector[i - 1][j] || check_vector[i - 1][j - a[i]];
			}
			else
			{
				check_vector[i][j] = check_vector[i - 1][j];
			}
		}
	}

	printing_available_subsets(a, n - 1, s, subset);
	return 0;
}



int main()
{
	int a[] = { 5, 23, 27, 37, 48, 51, 63, 67, 71, 75, 79, 83, 89, 91, 101, 112, 121, 132, 137, 141, 143,
147, 153, 159, 171, 181, 190, 191};
	std::vector<int> subset = {};
	int n = sizeof(a) / sizeof(a[0]);
	int knapsack_value = 762;
	knapsack(a, n, knapsack_value, subset);
	myfile.open("results.txt", std::ios::app);
	myfile << str << std::endl;

	return 0;
}

