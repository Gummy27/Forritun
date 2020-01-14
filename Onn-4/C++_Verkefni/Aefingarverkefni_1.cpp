#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

/*
// Æfing 1
int main(void){
	float x;
	float h = 1./2;
	float pi = 3.14159265359;
	float y, part1, part2;

	cin >> x;
	y = ((x*x) / ( (pi*pi) * (x*x+h)))*
		(1+ ((x*x) / ((pi*pi) * ((x*x-h)*(x*x-h)))));

	cout << y << endl;

	return 0;
}

// Æfing 2
int main(void){
	int i, j, k;

	cout << "Enter i: ";
	cin >> i;
	cout << "Enter j: ";
	cin >> j;

	i += 2;
	j -= i;
	k = i / j;
	k += k;
	k--;
	j = k % i;
	k += k + i;
	k += k / j;
	k = k*k*k;
	k += i * j;

	cout << k << endl;

	return 0;
}

// Æfing 3
int main(void){
	int value;
	bool answer;
	
	cin >> value;

	answer = (value >= 0 && value < 10) || 
			 (value * 2 < 20 && value -2 > -2) ||
			 (value - 1 > 1 && value / 2 < 10) ||
			 (value == 111);

	cout << (answer ? "That's True :)" : "That's not True :(") << endl;
}

// Æfing 4
int main(void){
	float nr = 2.13456;

	cout << setprecision(2) << 2.3 << endl;
	cout << setprecision(3) << 2.3 << endl;
	cout << setprecision(7) << 2.123456 << endl;
	cout << setprecision(3) << 2.123456 << endl;
	cout << setprecision(1) << 2.123456 << endl;
}

// Æfing 5
int main(void){
	float x = 1011, y = 1112;
	if(x / 1 == y / 1){
		cout << "Results are equal (by 0.0000001 epsilon)" << endl;
	}
	else{
		cout << "Results are not equal (by 0.0000001 epsilon)" << endl;
	}
}

// Æfing 6
int main(void){
	int x, z, y, i;

	cin >> x;
	cin >> z;
	cin >> y;
	cin >> i;

	if(x >= 1 && x < 255 && z >= 1 && z < 255 && y >= 1 && y < 255 && i >= 1 && i < 255){
		char d = '.';
		string ip = to_string(x)+d+to_string(z)+d+to_string(y)+d+to_string(i);
		cout << ip << endl;
	}
	else{
		cout << "This is not a valdi ip address" << endl;
	}

} 
*/

int main(void){
	int input = 5;

	string binary;
	int i = 1;
	for(i; i < input; i *= 2){
		cout << i << endl;
	}
	i /= 2;

	for(i; i > 0; i /= 2){
		cout << i - input << " : "<< i << " : " << input << endl;
		if(input - 1 >= 0 && input > 0){
			binary += "1";
			input -= i;
		} 
		else{
			binary += "0";
		}
	}

	cout << binary <<  endl;
	return 0;
}