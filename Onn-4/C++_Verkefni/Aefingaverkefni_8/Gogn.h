#pragma once

#include <iostream>

using namespace std;

class Gogn {
    private:
        int id;
        int numer;
    public:
        Gogn();
        Gogn(int id, int numer);

        int getID();
        void prentaGogn();

        int getNumer();
        bool operator<(Gogn& other);
        bool operator>(Gogn& other);
        bool operator<=(Gogn& other);
        bool operator>=(Gogn& other);

        bool operator==(Gogn& other);
        bool operator!=(Gogn& other);
};

