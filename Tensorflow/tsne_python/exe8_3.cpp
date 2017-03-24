#include <string>
#include <iostream>
#include <fstream>
using namespace std;

istream& getAndput(istream&);

int main()
{
	ifstream myfile1;
	myfile1.open("mnist2500_X2.txt");
	ifstream myfile2;
	myfile2.open("mnist2500_labels2.txt");
	//myfile.close();
	char buff[2048];
	char buff2[2048];
	int i = 0;
	if(!myfile1)
	{
		cout << "unable to open myfile";
		exit(1);
	}
	int max = 0;
	ofstream outfile("mnist2500_X.txt");
	ofstream outfile2("mnist2500_labels.txt");
	int length = 150;
	int width = 40;
	while(!myfile1.eof())
	{
		myfile1.getline(buff,2048,'\n');
		myfile2.getline(buff2, 2048,'\n');
		int temp = strlen(buff);
		string ans = buff;
		int count = 0;

		for(int x = 0; x < temp; x ++)
		{
			if(buff[x] == ' ')
				count ++;
		}

		if(temp > 150 || count > 40)
			continue;
		else
			;
		string inner = "";
		//if(temp > max)
			//max = temp;
		// for(int i = temp; i < length; i ++)
		// {

		// 	//cout << i - temp << endl;
		// 	if((i - temp) % 2 == 0)
		// 	{
		// 		inner += " ";
		// 	}
		// 	else
		// 	{
		// 		inner += "0";
		// 	}
		// }
	

		int add = width - count;
		for(int x = 0; x < add; x ++)
		{
			ans += " 0.0";
		}

		if(count > max)
			max = count;
		string ans2 = buff2;
		ans2 += "\n";
		ans += inner + "\n";
		cout << "read line: " << ":" << ans << endl;
		outfile << ans;
		outfile2 << ans2;
	}
	cout << max << endl;
	myfile1.close();
	myfile2.close();
	return 0;
}