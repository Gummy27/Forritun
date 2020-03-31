#pragma once 

#include <iostream>
#include <string>

class Dyr {
    private:
        int id;
        std::string nafn;
    public:
        Dyr();
        Dyr(int id, std::string nafn);
        int getId();
        void setId(int id);
        std::string getNafn();
        void setNafn(std::string nafn);
        virtual void prenta();
        virtual ~Dyr() {} // þarf að vera til en ekki að útfæra
};