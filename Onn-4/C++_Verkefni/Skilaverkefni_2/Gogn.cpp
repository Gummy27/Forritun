#include "Gogn.h"

Gogn::Gogn(){
    this->verkefni = "";
    this->skolaVerkefni = false;
    this->mikilvaegi = 0;
};

Gogn::Gogn(string verkefni, bool skolaVerkefni, int mikilvaegi){
    this->verkefni = verkefni;
    this->skolaVerkefni = skolaVerkefni;
    this->mikilvaegi = mikilvaegi;
};

string Gogn::getVerkefni(){
    return this->verkefni;
};

bool Gogn::getSkolaverkefni(){
    return this->skolaVerkefni;
};

int Gogn::getMikilvaegi(){
    return this->mikilvaegi;
};

void Gogn::prentaGogn(){
    cout << this->verkefni << ", " 
         << (this->skolaVerkefni ? "skólaverkefni" : "ekki skólaverkefni") << ", "
         << "mikilvægi " << this->mikilvaegi << "." << endl;
}

bool Gogn::operator<(Gogn& other){
    return this->mikilvaegi < other.mikilvaegi;
};

bool Gogn::operator>(Gogn& other){
};

bool Gogn::operator<=(Gogn& other){
};

bool Gogn::operator>=(Gogn& other){
};


bool Gogn::operator==(Gogn& other){
};

bool Gogn::operator!=(Gogn& other){
};

