#include "Dyragardur.h"

Dyragardur::Dyragardur() {
    this->staerdFylkis = 0;
    this->fjoldi = 0;
    this->dyragardur = new Dyr*[this->staerdFylkis]();
}

Dyragardur::Dyragardur(int upphafsstaerd) {
    // TODO: Fallið frumstillir gagnabreytur klasans.
    this->staerdFylkis = upphafsstaerd;
    this->fjoldi = 0;
    this->dyragardur = new Dyr*[this->staerdFylkis]();
}

void Dyragardur::skraDyr(Dyr* dyr) {
    // TODO: Fallið finnur laust pláss í fylkinu og skrári dyr í það.
    //       Ef ekkert laust pláss er í fylkinu er fylkið stækkað
    if(this->fjoldi < this->staerdFylkis) {
        this->dyragardur[fjoldi++] = dyr;
    } else {
        Dyr** temp = new Dyr*[this->staerdFylkis+2];
        for(int i = 0; i < this->staerdFylkis; i++){
            temp[i] = this->dyragardur[i];
        }
        delete [] this->dyragardur;
        this->dyragardur = temp;
        this->staerdFylkis += 2;
        this->dyragardur[fjoldi++] = dyr;
    }
}

void Dyragardur::skraHund(int id, std::string nafn, int hlydnieinkunn, std::string matur) {
    // TODO: Fallið skráir hund í listann
    Hundur* hundur = new Hundur(id, nafn, hlydnieinkunn, matur);
    skraDyr(hundur);
}

void Dyragardur::skraKott(int id, std::string nafn, std::string eigandi) {
    Kottur* kottur = new Kottur(id, nafn, eigandi);
    skraDyr(kottur);
}

void Dyragardur::afskraDyr(int id) {
    // TODO: Fallið eyðir dýri úr listanum og setur nullptr í stakið sem dýrið var í.
    for(int i = 0; i < this->staerdFylkis; i++){
        if(this->dyragardur[i]->getId() == id){
            delete dyragardur[i];
            dyragardur[i] = nullptr;
        }
    }
}

void Dyragardur::prenta() {
    // TODO: Fallið skrifar út öll dýrin sem eru í listanum.
    for(int i = 0; i < this->staerdFylkis; i++){
        if(dyragardur[i] != nullptr){
            dyragardur[i]->prenta();
        }
    }
}

Dyragardur::~Dyragardur() {
    // TODO: Fallið eyðir öllum dýrunum sem eru í listanum og eyðir svo listanum.
}

 // TODO?: Frjálst val, önnur föll og breytur sem gæti verið gott að eiga?
