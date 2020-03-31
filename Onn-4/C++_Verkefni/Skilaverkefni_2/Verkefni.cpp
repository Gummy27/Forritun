#include "Verkefni.h"

Verkefni::Verkefni(){
    this->verkefni = "";
    this->skolaVerkefni = false;
    this->mikilvaegi = 0;
};

Verkefni::Verkefni(string verkefni, bool skolaVerkefni, int mikilvaegi){
    this->verkefni = verkefni;
    this->skolaVerkefni = skolaVerkefni;
    this->mikilvaegi = mikilvaegi;
};

string Verkefni::getVerkefni(){
    return this->verkefni;
};

bool Verkefni::getSkolaverkefni(){
    return this->skolaVerkefni;
};

int Verkefni::getMikilvaegi(){
    return this->mikilvaegi;
};

void Verkefni::prentaVerkefni(){
    cout << this->verkefni << ", " 
         << (this->skolaVerkefni ? "skólaverkefni" : "ekki skólaverkefni") << ", "
         << "mikilvægi " << this->mikilvaegi << "." << endl;
}

bool Verkefni::operator<(Verkefni& other){
    if (this->getSkolaverkefni() + other.getSkolaverkefni() == 1) {
        if(this->getSkolaverkefni()) {
            return false;
        } else {
            return true;
        } 
    } else {
        return this->mikilvaegi < other.mikilvaegi;
    }
};

bool Verkefni::operator>(Verkefni& other){
    return !(*this < other);
};

bool Verkefni::operator<=(Verkefni& other){
    return !(*this > other);
};

bool Verkefni::operator>=(Verkefni& other){
    return !(*this < other);
};


bool Verkefni::operator==(Verkefni& other){
    if(this->getSkolaverkefni() + other.getSkolaverkefni() != 1) {
        if(this->mikilvaegi == other.mikilvaegi){
            return true;
        }
    }
    return false;
};

bool Verkefni::operator!=(Verkefni& other){
    return !(*this == other);
};

