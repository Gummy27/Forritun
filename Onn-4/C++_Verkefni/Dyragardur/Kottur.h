#pragma once

#include <iostream>
#include <string>

#include "Dyr.h"

class Kottur : public Dyr {
    private:
        std::string eigandi;
    public:
        Kottur();
        Kottur(int id, std::string nafn, std::string eigandi);
        std::string getEigandi();
        void setEigandi(std::string eigandi);
        void prenta();
};