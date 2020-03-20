#include "RadadurListi.h"

RadadurListi::RadadurListi(){
    this->head = nullptr;
};

void RadadurListi::setjaILista(string verkefni, bool skolaverkefni, int mikilvaegi){
    if(this->head == nullptr){
        this->head = new GognNode(verkefni, skolaverkefni, mikilvaegi);
    } else {
        GognNode* nyttStak = new GognNode(verkefni, skolaverkefni, mikilvaegi);
        if(nyttStak->data < this->head->data){
            nyttStak->next = this->head;
            this->head = nyttStak;
        } else {
            GognNode* current = this->head;
            GognNode* prev = this->head;
            while(current && current->data < nyttStak->data) {
                prev = current;
                current = current->next;
            }
            prev->next = nyttStak;
            nyttStak->next = current;
        }
    }
};

void RadadurListi::prentaLista(){
    GognNode* current = this->head;
    while(current) {
        current->data.prentaGogn();
        current = current->next;
    }
};


RadadurListi::~RadadurListi(){
    GognNode* newHead;
    while(this->head) {
        newHead = this->head->next;
        delete this->head;
        this->head = newHead;
    }
};
