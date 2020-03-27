#include "Dyr.h"

Dyr::Dyr() {
    this->id = -1;
    this->nafn = "";
}

Dyr::Dyr(int id, std::string nafn) {
    this->id = id;
    this->nafn = nafn;
}

int Dyr::getId() {
    return this->id;
}

void Dyr::setId(int id) {
    this->id = id;
}

std::string Dyr::getNafn() {
    return this->nafn;
}

void Dyr::setNafn(std::string nafn) {
    this->nafn = nafn;
}

void Dyr::prenta() {
    std::cout << "Dýr: " << this->id << ", " << this->nafn;
}
