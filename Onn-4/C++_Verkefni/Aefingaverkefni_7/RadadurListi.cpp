#include "RadadurListi.h"
#include <iostream>

using namespace std;

RadadurListi::RadadurListi() {
    this->head = nullptr;
}

void RadadurListi::setjaILista(int id, int numer) {
    if(this->erILista(id)) return;
    if(this->head == nullptr) {
        this->head = new GognNode(id, numer);
    } else {
        GognNode* nyttStak = new GognNode(id, numer);
        if(this->head->data.getID() > id) {
            nyttStak->next = this->head;
            this->head = nyttStak;
        } else {
            GognNode* current = this->head;
            GognNode* prev = this->head;
            while(current && current->data.getID() < id) {
                prev = current;
                current = current->next;
            }
            prev->next = nyttStak;
            nyttStak->next = current;
        }
    }
}

// fallið eyðir staki með id úr listanum
// Gera síðast. Er flóknasta af öllum.
void RadadurListi::eydaUrLista(int id) {
    if(!this->erILista(id)) 
        return;
    if(this->head->data.getID() == id) {
        this->head = this->head->next;
    } else {
        GognNode* current = this->head;
        GognNode* prev = nullptr;
        while(current != nullptr){
            if(current->data.getID() == id){
                prev->next = current->next;
                delete [] current;
            }
            prev = current;
            current = current->next;
        }
    }
}

// fallið skilar true ef stak með id er í listanum annars false
bool RadadurListi::erILista(int id) {
    GognNode* current = this->head;
    while(current != nullptr){
        if(current->data.getID() == id){
            return true;
        }
        current = current->next;
    }
    return false;
}

// fallið skrifar listann út á skjá
void RadadurListi::prentaLista() {
    GognNode* current = this->head;
    while(current != nullptr){
        cout << "Id: " << current->data.getID() 
             << ", Data: " << current->data.getNumer() << endl;

        current = current->next;
    }
    cout << endl;
}

// destructorinn eyðir öllum Node-unum úr listanum
RadadurListi::~RadadurListi() {
    // TODO
}