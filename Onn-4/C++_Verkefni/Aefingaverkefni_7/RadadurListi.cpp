#include "RadadurListi.h"

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
        // TODO
    } else {
        // TODO 
    }
}

// fallið skilar true ef stak með id er í listanum annars false
bool RadadurListi::erILista(int id) {
    // TODO
}

// fallið skrifar listann út á skjá
void RadadurListi::prentaLista() {
    GognNode* current = this->head;
    while(current->next){
        cout << current->data;
        current = current->next;
    }
    cout << endl;
}

// destructorinn eyðir öllum Node-unum úr listanum
RadadurListi::~RadadurListi() {
    // TODO
}