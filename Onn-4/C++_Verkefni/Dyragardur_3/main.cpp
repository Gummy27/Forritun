#include <iostream>

#include "Dyragardur.h"

int main() {
    Dyragardur d;

    Dyr* fluffy = new Kottur(20, "Fluffy", "Konni");

    d.skraDyr(fluffy);
    d.skraHund(10, "Lotta", 3, "allt");
    d.skraKott(60, "Mr. Jinx", "Jack");
    d.skraHund(30, "Snati", 8, "ABC hundamatur");
    d.prenta(); // Ætti að skrifa út:
        // Hundur: 10, Lotta, borðar allt, einkunn: 3
        // Köttur 60, Mr. Jinx, eigandi: Jack
        // Hundur: 30, Snati, borðar ABC hundamatur, einkunn: 8
        // Köttur 20, Fluffy, eigandi: Konni
    std::cout << std::endl;
    d.afskraDyr("abc"); // ætti ekki að gera neitt þar sem ekkert dýr er skráð sem "abc"
    d.skraKott(40, "Grettir", "Jón");
    d.skraHund(50, "Snotra", 7, "grænmeti");
    d.afskraDyr("Grettir");
    std::cout << std::endl;
    d.prenta(); // Ætti að skrifa út:
        // Hundur: 10, Lotta, borðar allt, einkunn: 3
        // Köttur 60, Mr. Jinx, eigandi: Jack
        // Hundur: 30, Snati, borðar ABC hundamatur, einkunn: 8
        // Hundur: 50, Snotra, borðar grænmeti, einkunn: 7
        // Köttur 20, Fluffy, eigandi: Konni
    return 0;
};