#include "VerkefnaListi.h"

VerkefnaListi::VerkefnaListi(){
    this->head = nullptr;
};

void VerkefnaListi::setjaILista(string verkefni, bool skolaverkefni, int mikilvaegi){
    if(this->head == nullptr){
        this->head = new GognNode(verkefni, skolaverkefni, mikilvaegi);
    } else {
        GognNode* nyttStak = new GognNode(verkefni, skolaverkefni, mikilvaegi);
        if(this->head->data < nyttStak->data){
            nyttStak->next = this->head;
            this->head = nyttStak;
        } else {
            GognNode* current = this->head;
            GognNode* prev = this->head;
            while(current && current->data > nyttStak->data) {
                prev = current;
                current = current->next;
            }
            prev->next = nyttStak;
            nyttStak->next = current;
        }
    }
};

void VerkefnaListi::setjaILista(Verkefni verkefni){
    setjaILista(verkefni.getVerkefni(), verkefni.getSkolaverkefni(), verkefni.getMikilvaegi());
};

void VerkefnaListi::prentaOllVerkefni(){
    GognNode* current = this->head;
    while(current) {
        current->data.prentaVerkefni();
        current = current->next;
    }
};


void VerkefnaListi::prentaSkolaverkefni(){
    GognNode* current = this->head;
    while(current) {
        if(current->data.getSkolaverkefni()){
            current->data.prentaVerkefni();
        }
        current = current->next;
    }
};

void VerkefnaListi::prentaEkkiSkolaverkefni(){
    GognNode* current = this->head;
    while(current) {
        if(!current->data.getSkolaverkefni()){
            current->data.prentaVerkefni();
        }
        current = current->next;
    }
};

Verkefni VerkefnaListi::faNaestaVerkefni(){
    Verkefni toBePopped = this->head->data;
    this->head = this->head->next;
    return toBePopped;
};

VerkefnaListi::~VerkefnaListi(){
    GognNode* newHead;
    while(this->head) {
        newHead = this->head->next;
        delete this->head;
        this->head = newHead;
    }
};
