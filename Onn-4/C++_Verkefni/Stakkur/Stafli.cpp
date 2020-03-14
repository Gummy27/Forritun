#include "Stafli.h"

Stafli::Stafli(){
    this->bendill = 0;
};

void Stafli::push(int data){
    this->staflinn[this->bendill++] = data;
};

int Stafli::pop(){
    return this->staflinn[--this->bendill];
};

int Stafli::peek(){
    return this->staflinn[this->bendill - 1];
};

void Stafli::prenta(){
    for(int i = 0; i < this->bendill; i++){
        cout << this->staflinn[i] << " - ";
    }
    cout << endl;
};
