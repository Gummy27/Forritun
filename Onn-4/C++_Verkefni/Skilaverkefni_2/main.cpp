#include <iostream>

#include "VerkefnaListi.h"

using namespace std;

int main(){
    Verkefni v1("Labba með hundinn", false, 5);
    Verkefni v2("Ritgerð í íslensku", true, 3);
    Verkefni v3("Forritunarverkefni", true, 5);

    cout << (v1 < v2) << endl; // Ætti að skrifa út 1
    cout << (v3 > v2) << endl; // Ætti að skrifa út 1
    cout << (v1 >= v3) << endl; // Ætti að skrifa út 0
    cout << endl;

    VerkefnaListi verk;
    verk.setjaILista(v1);
    verk.setjaILista(v3);
    verk.setjaILista(v2);

    verk.prentaOllVerkefni(); // ætti að skrifa út
        // Verkefni: Forritunarverkefni, skólaverkefni: Já, mikilvægi: 5
        // Verkefni: Ritgerð í íslensku, skólaverkefni: Já, mikilvægi: 3
        // Verkefni: Labba með hundinn, skólaverkefni: Nei, mikilvægi: 5 
    cout << endl;
    
    verk.faNaestaVerkefni().prentaVerkefni(); // ætti að skrifa út:
        // Verkefni: Forritunarverkefni, skólaverkefni: Já, mikilvægi: 5
    
    verk.faNaestaVerkefni().prentaVerkefni(); // ætti að skrifa út:
        // Verkefni: Ritgerð í íslensku, skólaverkefni: Já, mikilvægi: 3
    cout << endl;

    verk.setjaILista("Fara út með ruslið", false, 6);
    verk.setjaILista("Borða", false, 6);
    verk.setjaILista("Gefa kettinum að borða", false, 5);

    verk.prentaOllVerkefni(); // ætti að skrifa út:
        // Verkefni: Fara út með ruslið, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Borða, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Labba með hundinn, skólaverkefni: Nei, mikilvægi: 5
        // Verkefni: Gefa kettinum að borða, skólaverkefni: Nei, mikilvægi: 5    
    cout << endl;

    verk.setjaILista("Gera smá HTML", true, 8);
    verk.setjaILista("Reikna slatta", true, 7);
    verk.setjaILista("Gera smá c++", true, 9);
    verk.prentaOllVerkefni(); // ætti að skrifa út:
        // Verkefni: Gera smá c++, skólaverkefni: Já, mikilvægi: 9
        // Verkefni: Gera smá HTML, skólaverkefni: Já, mikilvægi: 8
        // Verkefni: Reikna slatta, skólaverkefni: Já, mikilvægi: 7
        // Verkefni: Fara út með ruslið, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Borða, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Labba með hundinn, skólaverkefni: Nei, mikilvægi: 5
        // Verkefni: Gefa kettinum að borða, skólaverkefni: Nei, mikilvægi: 5
    cout << endl;

    verk.prentaSkolaverkefni(); // ætti að skrifa út:
        // Verkefni: Gera smá c++, skólaverkefni: Já, mikilvægi: 9
        // Verkefni: Gera smá HTML, skólaverkefni: Já, mikilvægi: 8
        // Verkefni: Reikna slatta, skólaverkefni: Já, mikilvægi: 7
    cout << endl;

    verk.prentaEkkiSkolaverkefni(); // ætti að skrifa út:
        // Verkefni: Fara út með ruslið, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Borða, skólaverkefni: Nei, mikilvægi: 6
        // Verkefni: Labba með hundinn, skólaverkefni: Nei, mikilvægi: 5
        // Verkefni: Gefa kettinum að borða, skólaverkefni: Nei, mikilvægi: 5
}