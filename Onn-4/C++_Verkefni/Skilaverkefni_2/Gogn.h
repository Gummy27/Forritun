#pragma once

#include <iostream>
#include <string>

using namespace std;

class Gogn{
    private:
        string verkefni;
        bool skolaVerkefni;
        int mikilvaegi;

    public:
        Gogn();
        Gogn(string verkefni, bool skolaVerkefni, int mikilvaegi);

        string getVerkefni();
        bool getSkolaverkefni();
        int getMikilvaegi();

        void prentaGogn();

        bool operator<(Gogn& other);
        bool operator>(Gogn& other);
        bool operator<=(Gogn& other);
        bool operator>=(Gogn& other);

        bool operator==(Gogn& other);
        bool operator!=(Gogn& other);

};