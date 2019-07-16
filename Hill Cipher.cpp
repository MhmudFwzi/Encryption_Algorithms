#include <iostream>.
#include <string>
#include <math.h>
using namespace std;
 
int getNumber(char c)
{
	return (int(c) - 65) % 26;
}
char getChar(int x)
{
	return char( (x % 26) + 65 );
}
string messageprocessing(string s, int d)
{
	while (s.size() % d != 0)
	{
		s += "X";
	}
	for (int i = 0; i < s.size(); i++)
	{
		s[i] = s[i] - 'A';
	}
	return s;
}
int main()
 
{
//Initialization & Padding
	int n;
	int Key[100][100];
	cin >> n;
    int  SQRTN = sqrt(n);
	long long x;
	for (int i = 0; i < SQRTN; i++)
	{
		for (int j = 0; j < SQRTN; j++)
		{
			cin >> x;
			Key[i][j] = x % 26;
		}
	}
	string message;
	cin >> message;
	message = messageprocessing(message, SQRTN);
	long long RESULT[100][100] = { 0 };
 
	for (int i = 0; i < message.size(); i+=SQRTN)
	{
		for (int j = 0; j < SQRTN; j++)
		{
			for (int k = 0; k < SQRTN; k++)
			{
				RESULT[i / SQRTN][j] += (Key[j][k] * message[i + k])%26;
				RESULT[i / SQRTN][j] = RESULT[i / SQRTN][j] % 26;
			}
		}
	}
	string Output = "";
	for (int i = 0; i < (message.size()/SQRTN); i++)
	{
		for (int j = 0; j < SQRTN; j++)
		{
			Output += char(RESULT[i][j] + 'A');
		}
	}
	cout << Output;
	 
	return 0;
}
