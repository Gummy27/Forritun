#pragma once

#include <string>

class Leikmadur {
    private:
        int id;
        std::string nafn;

    public:
        Leikmadur(int id, std::string nafn);

        int getId();
        void setId(int id);

        std::string getNafn();
        void setNafn(std::string nafn);
};