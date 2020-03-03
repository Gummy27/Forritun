#include <iostream>
#include <string>
#include "Nemandi.h"
#include "Afangi.h"

using namespace std;

int main(){
    Nemandi geir = Nemandi(11, "Geir");
    geir.skra_afanga(33, "GAGN", 2.43);
    geir.skra_afanga(34, "FORR", 3.59);
    geir.skra_afanga(35, "ROBO", 10  );
    geir.skra_afanga(36, "KEST", 6.249);

    geir.uppfaeraEinkunn(34, 4.49);

    geir.eyda_afanga(33);

    geir.prenta();
    return 0;
}