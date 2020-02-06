#include <iostream>
#include <bitset>

using namespace std;

int main(){
    unsigned short int binary;
    bool ispalindrome = true;

    cout << "value: ";
    cin >> binary;

    int binary1 = binary, binary2 = binary;
    int bit;

    for(int x = 0; x < 8; x++){
        bit = binary1<<1;
        cout << bitset<16>(binary2) << " : " << bitset<16>(binary1) << " = " << bit << endl;
        if(((binary1<<1)^(binary2>>1))){
            ispalindrome = false;
            break;
        }
        binary1 = binary1 << 1;
        binary2 = binary2 >> 1;
    }

    if(ispalindrome){
        cout << binary << " is a bitwise palindrome" << endl;
    } else {
        cout << binary << " is not a bitwise palindrome" << endl;
    }
}





/*
int main(){
    int i = 0;
    unsigned long binary;

    cout << "Decimal number: ";
    cin >> binary;
    for(int x = 0; x < 32; x++){
        i += binary & 1;
        binary = binary >> 1;
    }
    cout << i << endl;
}
*/