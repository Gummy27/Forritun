#pragma once

#include <iostream>
#include <string>

#include "Dyr.h"
#include "Hundur.h"
#include "Kottur.h"

class Dyragardur {
    private:
        Dyr** dyragardur;
        int staerdFylkis;
        int fjoldi;
        // TODO?: Frjálst val, önnur föll og breytur sem gæti verið gott að eiga?  
    public:
        Dyragardur();
        Dyragardur(int upphafsstaerd);
        void skraDyr(Dyr* dyr);
        void skraHund(int id, std::string nafn, int hlydnieinkunn, std::string matur);
        void skraKott(int id, std::string nafn, std::string eigandi);
        void afskraDyr(int id);
        void prenta();
        ~Dyragardur();
};