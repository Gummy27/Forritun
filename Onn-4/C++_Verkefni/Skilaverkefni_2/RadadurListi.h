#pragma once

#include "GognNode.h"

class RadadurListi {
    private:
        GognNode* head;

    public:
        RadadurListi();
        void setjaILista(string verkefni, bool skolaverkefni, int mikilvaegi);
        void prentaLista();

        ~RadadurListi();
};