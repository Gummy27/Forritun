#include "Leikmadur.h"
#include <string>

Leikmadur::Leikmadur(int id, std::string nafn){
    this->id = id;
    this->nafn = nafn;
};

int Leikmadur::getId(){
    return this->id;
};

void Leikmadur::setId(int id){
    this->id = id;
};

std::string Leikmadur::getNafn(){
    return this->nafn;
};

void Leikmadur::setNafn(std::string nafn){
    this->nafn = nafn;
};
