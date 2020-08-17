#pragma once

#include <string>

class Stada {
    private:    
        char stada;
        std::string nafn;
    public:

        char getStada();
        std::string getNafn();
        
        void setStada(char stada);
        void setNafn(std::string nafn);


        Stada();
        Stada(char stada, std::string nafn);

};