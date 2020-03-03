#include "Nemandi.h"
#include "Afangi.h"

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

int Nemandi::empty_in_array(){
    for(unsigned int i = 0; i < this->size; i++){
        if(this->afangar[i].get_id() == 0){
            return i;
        }
    }
    return -1;
}

void Nemandi::add_space(){
    Afangi* temp = new Afangi[size+2];

    for(int i = 0; i < size; i++){
        temp[i] = this->afangar[i];
    }

    temp[-2] = Afangi();
    temp[-1] = Afangi();

    delete [] this->afangar;

    this->afangar = temp;

    this->size += 2;


};

void Nemandi::skra_afanga(int id, string name, double einkunn){
    int index = empty_in_array();
    cout << index << endl;
    if(index != -1){
        cout << "Kóðinn kemur hingað!" << endl;
        this->afangar[index] = Afangi(id, name, einkunn);
    }
    else{
        Nemandi::add_space();
        index = empty_in_array();
        this->afangar[index] = Afangi(id, name, einkunn);
    }

};

void Nemandi::get_afangar(){
    for(int i = 0; i < this->size; i++){
        cout << i << endl;
        if(this->afangar[i].get_id() != 0){
            cout << this->afangar[i].get_id() << ". " 
                 << this->afangar[i].get_name() << " : " 
                 << this->afangar[i].get_einkunn() << endl;
        }
    }
}
