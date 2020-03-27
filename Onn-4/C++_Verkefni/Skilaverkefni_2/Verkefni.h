#pragma once

#include <iostream>
#include <string>

using namespace std;

class Verkefni{
    private:
        string verkefni;
        bool skolaVerkefni;
        int mikilvaegi;

    public:
        Verkefni();
        Verkefni(string verkefni, bool skolaVerkefni, int mikilvaegi);

        string getVerkefni();
        bool getSkolaverkefni();
        int getMikilvaegi();

        void prentaVerkefni();

        bool operator<(Verkefni& other);
        bool operator>(Verkefni& other);
        bool operator<=(Verkefni& other);
        bool operator>=(Verkefni& other);

        bool operator==(Verkefni& other);
        bool operator!=(Verkefni& other);

};