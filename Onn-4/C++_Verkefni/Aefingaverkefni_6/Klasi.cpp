#include "Klasi.h"


Klasi::Klasi(){
    this->tala = 0;
    this->texti = "";
};

Klasi::Klasi(int tala, string texti){
    this->tala = tala;
    this->texti = texti;
};


int Klasi::gettTala(){ return this->tala; };

void Klasi::setTala(int tala){ this->tala = tala; };


string Klasi::getTexti(){ return this->texti; };

void Klasi::setTexti(string texti){ this->texti = texti;};

bool Klasi::operator>(Klasi& other){ return this->tala > other.tala; };

bool Klasi::operator<(Klasi& other){ return other > *this; };


bool Klasi::operator>=(Klasi& other){ return !(*this < other); };

bool Klasi::operator<=(Klasi& other){ return !(*this > other); };


bool Klasi::operator==(Klasi& other){ return this->tala == other.tala; };

bool Klasi::operator!=(Klasi& other){ return !(*this == other); };

ostream& operator<<(ostream& ostr, Klasi& k){
    return ostr << "Tala: " << k.gettTala() << ", texti: " << k.getTexti();
}