#include "Gogn.h"

Gogn::Gogn() {
    this->id = -1;
    this->numer = -1;
}

Gogn::Gogn(int id, int numer) {
    this->id = id;
    this->numer = numer;
}

int Gogn::getID() {
    return this->id;
}

int Gogn::getNumer() {
    return this->numer;
}

void Gogn::prentaGogn() {
    cout << "ID: " << this->id << ", Numer: " << this->numer << endl;
}
