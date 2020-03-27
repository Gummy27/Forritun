#include "Kottur.h"

Kottur::Kottur() {
    this->eigandi = "";
}

Kottur::Kottur(int id, std::string nafn, std::string eigandi) : Dyr(id, nafn) {
    this->eigandi = eigandi;
}

std::string Kottur::getEigandi() {
    return this->eigandi;
}

void Kottur::setEigandi(std::string eigandi) {
    this->eigandi = eigandi;
}

void Kottur::prenta() {
    std::cout << "Kottur " << this->getId() << ", " << this->getNafn() 
            << ", eigandi: " << this->eigandi << std::endl;
}
