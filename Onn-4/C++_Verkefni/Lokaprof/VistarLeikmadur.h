#pragma once

#include "Leikmadur.h"
#include "Stada.h"

class VistarLeikmadur : public Leikmadur {
    private:
        int stig;
        Stada stada;
    public:
        VistarLeikmadur(int id, std::string nafn, int stig, Stada stada);

        int getStig();
        void setStig(int stig);

        Stada getStada();
        void setStada(Stada stada);

        std::string getAllt();

        bool operator<(VistarLeikmadur& other);
};
