#include "Nemandi.h"
#include "Afangi.h"
#include <cmath>

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

double Nemandi::round_up(double tala, int aukastafir){
    double round_number = round(tala * pow(10, aukastafir)) / 10;
    return round_number;
};

int Nemandi::empty_in_array(){
    for(int i = 0; i < this->size; i++){
        if(this->afangar[i].get_id() == 0){
            return i;
        }
    }
    return -1;
}

void Nemandi::add_space(){
    Afangi* temp = new Afangi[size+2];
    
    for(int i = 0; i < this->size; i++){
        temp[i] = this->afangar[i];
    }

    delete [] this->afangar;

    this->afangar = temp;

    this->size += 2;


};

void Nemandi::skra_afanga(int id, string name, double einkunn){
    int index = empty_in_array();
    if(index != -1){
        this->afangar[index] = Afangi(id, name, einkunn);
    }
    else{
        Nemandi::add_space();
        index = empty_in_array();
        this->afangar[index] = Afangi(id, name, einkunn);
    }

};

void Nemandi::eyda_afanga(int id){
    for(int i = 0; i < this->size; i++){
        if(this->afangar[i].get_id() == id){
            this->afangar[i] = Afangi();
        }
    }
}

void Nemandi::prenta(){
    double grades = 0;
    double classes = 0;

    cout << "Nemandi: " << this->name << "(id: " << this->id << "), áfangar:" << endl;
    for(int i = 0; i < this->size; i++){
        if(this->afangar[i].get_id() != 0){
            cout << "ID: "      << this->afangar[i].get_id()                   << ", " 
                 << "nafn: "    << this->afangar[i].get_name()                 << ", " 
                 << "einkunn: " << round_up(this->afangar[i].get_einkunn(), 1) << endl;
            grades += afangar[i].get_einkunn();
            classes++;
        }
    }

    /*
    int temp = (grades / classes) * 10;
    double temp2 = temp;
    double medaleinkunn = temp2 / 10;
    */
    cout << "Meðaleinkunn: " << round_up(grades / classes, 1) << endl;
}

void Nemandi::uppfaeraEinkunn(int id, double einkunn){
    for(int i = 0; i < this->size; i++){
        if(this->afangar[i].get_id() == id){
            afangar[i].set_einkunn(einkunn);
            break;
        }
    }
};
