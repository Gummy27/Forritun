#pragma once

#include <iostream>
#include <string>

#include "Dyr.h"
#include "Hundur.h"
#include "Kottur.h"

#include "DyrNode.h"

class Dyragardur {
    private:
        DyrNode** dyragardur;
        int staerdFylkis;
        // TODO?: Frjálst val, önnur föll og breytur sem gæti verið gott að eiga?  
        int hash(Dyr* dyr);
        int hash(std::string nafn);
    public:
        Dyragardur();
        Dyragardur(int upphafsstaerd);
        void skraDyr(Dyr* dyr);
        void skraHund(int id, std::string nafn, int hlydnieinkunn, std::string matur);
        void skraKott(int id, std::string nafn, std::string eigandi);
        void afskraDyr(std::string nafn);
        void prenta();
        ~Dyragardur();
};