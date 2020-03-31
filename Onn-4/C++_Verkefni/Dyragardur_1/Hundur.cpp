#include "Hundur.h"
#include <iostream>

Hundur::Hundur() {
    this->hlydnieinkunn = -1;
    this->matur = "";
}

Hundur::Hundur(int id, std::string nafn, int hlydnieinkunn, std::string matur) : Dyr(id, nafn) {
    // TODO: Fallið frumstillir gagnabreytur klasans.
    this->hlydnieinkunn = hlydnieinkunn;
    this->matur = matur;
}

int Hundur::getEinkunn() {
    // TODO: Fallið skilar hlydnieinkunn breytunni.
    return this->hlydnieinkunn;
}

void Hundur::setEinkunn(int einkunn) {
    // TODO: Fallið uppfærir hlýðnieinkunn breytuna.
    this->hlydnieinkunn = einkunn;
}

std::string Hundur::getMatur() {
    // TODO: Fallið skilar matur breytunni.
    return this->matur;
    }

void Hundur::setMatur(std::string matur) {
    // TODO: Fallið uppfærir matur breytuna.
    this->matur = matur;
}

void Hundur::prenta() {
    // TODO: Fallið skrifar innihalda klasans á skjáinn.
    std::cout << "Hundur " << this->getId() << ", " << this->getNafn()
              << ", " << getMatur() << ", einkunn: " << getEinkunn() << std::endl;
}
