#include <iostream>
#include <stdio.h>
#include <string>
 
using namespace std;
 
string v(string k, string m)
{
	int i = 0;
	while (k.size() < m.size())
	{
		k += k[i];
		i++;
	}
	return k;
}
 
int main()
{
	bool Onetimepad = false;
	string key, message,Vkey;
	cin >> key;
	cin >> message;
	if (key.size() == message.size())
		Onetimepad = true;
	//VIGENERE&VERNAM
	Vkey = v(key,message);
	string VigenereO = "Vigenere: ";
	string VernamO = "";
	for (int i = 0; i <	Vkey.size(); i++)
	{
		int VIGsum = message[i] + Vkey[i];
		int Vernam = message[i] ^ Vkey[i];
		if (VIGsum > 90) VIGsum = (VIGsum % 26) + 65;
		if (Vernam > 90) Vernam = (Vernam % 26) + 65;
		VigenereO += char(VIGsum);
		VernamO += char(Vernam);
	}
	cout << VigenereO << endl << "Vernam: ";
	for (int i = 0; i < VernamO.size(); i++)
		printf("%02X", VernamO[i]);
	if (Onetimepad == true) cout <<endl<< "One-Time Pad: YES";
	else cout <<endl<< "One-Time Pad: NO";
