#include "Nemandi.h"

Nemandi::Nemandi(int id){
    this->id = id;
};

Nemandi::Nemandi(int id, string name){
    this->id = id;
    this->name = name;
};

int Nemandi::get_id(){
    return this->id;
};

void Nemandi::set_id(int id){
    this->id = id;
};

string Nemandi::get_name(){
    return this->name;
};

void Nemandi::set_name(string name){
    this->name = name;
};

void Nemandi::skra_afanga(int id, string name, double einkunn){
    
};