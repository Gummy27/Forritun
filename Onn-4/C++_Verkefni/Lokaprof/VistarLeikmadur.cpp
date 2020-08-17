#include "VistarLeikmadur.h"
#include <iostream>

#include <string>

VistarLeikmadur::VistarLeikmadur(int id, std::string nafn, int stig, Stada stada) : Leikmadur(id, nafn) {
    this->stada = stada;
    this->stig = stig;
};

int VistarLeikmadur::getStig(){
    return this->stig;
};

void VistarLeikmadur::setStig(int stig){
    this->stig = stig;
};


Stada VistarLeikmadur::getStada(){
    return this->stada;
};

void VistarLeikmadur::setStada(Stada stada){
    this->stada = stada;
};

std::string VistarLeikmadur::getAllt(){
    std::string id = std::to_string(this->getId());
    std::string stig = std::to_string(this->getStig());
    return "Id: " + id + ", Nafn: " + this->getNafn() + ", Staða: " + this->getStada().getNafn() + ", Stig: " + stig;
};

bool VistarLeikmadur::operator<(VistarLeikmadur& other){
    return this->getStig() < other.getStig();
};

