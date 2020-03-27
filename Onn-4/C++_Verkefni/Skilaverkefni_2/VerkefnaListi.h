#pragma once

#include "GognNode.h"

class VerkefnaListi {
    private:
        GognNode* head;

    public:
        VerkefnaListi();
        void setjaILista(string verkefni, bool skolaverkefni, int mikilvaegi);
        void setjaILista(Verkefni verkefni);
        void prentaOllVerkefni();
        void prentaEkkiSkolaverkefni();
        void prentaSkolaverkefni();
        Verkefni faNaestaVerkefni();

        ~VerkefnaListi();
};