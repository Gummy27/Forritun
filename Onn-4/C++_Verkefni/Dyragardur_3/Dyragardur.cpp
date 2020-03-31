#include "Dyragardur.h"
#include <string>

Dyragardur::Dyragardur() {
    this->staerdFylkis = 3;
    this->dyragardur = new DyrNode*[this->staerdFylkis]();
}

Dyragardur::Dyragardur(int upphafsstaerd) {
    // TODO: Fallið frumstillir gagnabreytur klasans.
    this->staerdFylkis = upphafsstaerd;
    this->dyragardur = new DyrNode*[this->staerdFylkis]();
}


int Dyragardur::hash(Dyr* dyr){
    return this->hash(dyr->getNafn());
};

int Dyragardur::hash(std::string nafn){
    int indexSum = 0;
    for(int i = 0; i < nafn.length(); i++){
        indexSum += (int)nafn[i];
    }
    return indexSum % this->staerdFylkis;
};


void Dyragardur::skraDyr(Dyr* dyr) {
    // TODO: Fallið finnur laust pláss í fylkinu og skrári dyr í það.
    //       Ef ekkert laust pláss er í fylkinu er fylkið stækkað+
    int index = this->hash(dyr);
    if(this->dyragardur[index] == nullptr){
        this->dyragardur[index] = new DyrNode(dyr);
    } else {
        DyrNode* current = this->dyragardur[index];
        while(current->next) {
            current = current->next;
        }
        current->next = new DyrNode(dyr);
    }
}

void Dyragardur::skraHund(int id, std::string nafn, int hlydnieinkunn, std::string matur) {
    // TODO: Fallið skráir hund í listann
    this->skraDyr(new Hundur(id, nafn, hlydnieinkunn, matur));
}

void Dyragardur::skraKott(int id, std::string nafn, std::string eigandi) {
    this->skraDyr(new Kottur(id, nafn, eigandi));
}

void Dyragardur::afskraDyr(std::string nafn) {
    // TODO: Fallið eyðir dýri úr listanum og setur nullptr í stakið sem dýrið var í.
    int eydaIndex = this->hash(nafn);
    if(this->dyragardur[eydaIndex]->dyr->getNafn() == nafn){
        DyrNode* newHead = this->dyragardur[eydaIndex]->next;
        delete this->dyragardur[eydaIndex];
        this->dyragardur[eydaIndex] = newHead;
    } else {
        DyrNode* current = this->dyragardur[eydaIndex];
        DyrNode* prev = this->dyragardur[eydaIndex];
        while(current && current->dyr->getNafn() != nafn) {
            prev = current;
            current = current->next;
        }

        if(current){
            prev->next = current->next;
            delete current;
        }
    }
}

void Dyragardur::prenta() {
    // TODO: Fallið skrifar út öll dýrin sem eru í listanum.
    DyrNode* current;
    for(int i = 0; i < this->staerdFylkis; i++){
       current = this->dyragardur[i];
       while(current){
           // Gera sama og venjulega með current
       } 
    }
}

Dyragardur::~Dyragardur() {
    // TODO: Fallið eyðir öllum dýrunum sem eru í listanum og eyðir svo listanum.
}

 // TODO?: Frjálst val, önnur föll og breytur sem gæti verið gott að eiga?
