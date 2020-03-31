#pragma once

#include "Dyr.h"

class Hundur : public Dyr {
    private:
        int hlydnieinkunn;
        std::string matur;
    public:
        Hundur();
        Hundur(int id, std::string nafn, int hlydnieinkunn, std::string matur);
        int getEinkunn();
        void setEinkunn(int einkunn);
        std::string getMatur();
        void setMatur(std::string matur);
        void prenta();
};