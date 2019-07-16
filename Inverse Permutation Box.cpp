#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
	int S, Ptable[512], IPtable[512];
	cin >> S;
	for (int i = 1; i < S+1; i++)
	{
		cin >> Ptable[i];
		IPtable[Ptable[i]] = i;
		for (int j = 0; j < i; j++)
		{
			if (Ptable[i] == Ptable[j])
			{
				cout << "IMPOSSIBLE";
				return 0;
			}
		}
	}
	for (int i = 1; i < S+1; i++)
	{
		if (i == S)
		{
			cout << IPtable[i];
			break;
		}
		cout << IPtable[i]<<" ";
	}
}
