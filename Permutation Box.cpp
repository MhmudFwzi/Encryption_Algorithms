#include <iostream>
#include <string>
#include <math.h>
 
using namespace std;
 
string binary(int num)
{
	int rem;
	string bin = "";
	if (num == 1) return "1";
	if (num == 0) return "0";
    bin += binary(num / 2);
	rem = num % 2;
	if (rem == 0) bin += '0';
	if (rem == 1) bin += '1';
 
	return bin;
}
int bintodec(string s)
{
	int d = 0;
	int n;
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '0') n = 0;
		else n = 1;
		d += (n * pow(2, s.size() - 1 - i));
	}
	return d;
}
 
int main()
{
	//INPUT
	int S, Ptable[512], N, input;
	cin >> S;
	for (int i = 0; i < S; i++)
	{
		cin >> Ptable[i];
	}
	cin >> N;
	cin >> hex >> input;
 
	//CIPHERING
	string binin = binary(input);
	while (binin.size() != N)
	{
		string temp = binin;
		binin = "0" + temp;
	}
	string binout = "";
	for (int i = 0; i < S ; i++)
	{
		binout += binin[(Ptable[i] - 1)];
	}
	cout << hex << uppercase << bintodec(binout);
 
	
}
