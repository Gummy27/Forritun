#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void vista(){
    fstream file;
    file.open("baekur.txt", ios::out);

    if(!file){
        cout << "Villa kom upp! Bókin var ekki vistuð!" << endl;
    } else {
        cout << "This is kinda gay I won't lie!" << endl;
        file << "This is working!" << endl;
    }
};
int main()
{
  vista();
  
  return 0;
}