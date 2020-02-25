#include "Klasi.h"
#include <iostream>
#include <string>

using namespace std;

int main(){

    Klasi k(10, "abc");
    Klasi j(20, "cde");

    if(k < j) 
        cout << "K er minna en J" << endl;

    cout << k << " er minna en " << j << endl;
}