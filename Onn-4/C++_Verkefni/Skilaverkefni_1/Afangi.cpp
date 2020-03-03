#include "Afangi.h"

Afangi::Afangi(){
    this->id = 0;
    this->name = "";
    this->einkunn = 0;
};

Afangi::Afangi(int id, string name, double einkunn) {
    this->id = id;
    this->name = name;
    this->einkunn = einkunn;
};


int Afangi::get_id() {
    return this->id;
};

void Afangi::set_id(int id) {
    this->id = id;
};

string Afangi::get_name() {
    return this->name;
};

void Afangi::set_name(string name) {
    this->name = name;
};

double Afangi::get_einkunn() {
    return this->einkunn;
};

void Afangi::set_einkunn(double einkunn) {
    this->einkunn = einkunn;
};
