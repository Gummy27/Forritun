#include <iostream>
#include <string>
#include "Nemandi.h"
#include "Afangi.h"

using namespace std;

int main(){
    Nemandi Geir = Nemandi(1, "Geir");
    Geir.skra_afanga(1, "Forritun", 9.8);
    Geir.skra_afanga(2, "Vefþróun", 4.5);
    Geir.skra_afanga(3, "Kerfistjónun", 7.4);
    cout << "This code is indeed working!" << endl;

    Geir.get_afangar();

    cout << "This code is indeed working!" << endl;
    return 0;
}