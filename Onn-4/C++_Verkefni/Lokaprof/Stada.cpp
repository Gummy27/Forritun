#include "Stada.h"

Stada::Stada(){
    this->stada = 'x';
    this->nafn = "";
};

Stada::Stada(char stada, std::string nafn){
    this->stada = stada;
    this->nafn = nafn;
};

char Stada::getStada(){
    return this->stada;
};

std::string Stada::getNafn(){
    return this->nafn;
};


void Stada::setStada(char stada){
    this->stada = stada;
};

void Stada::setNafn(std::string nafn){
    this->nafn = nafn;
};
