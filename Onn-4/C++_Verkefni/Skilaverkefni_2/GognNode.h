#pragma once

#include "Gogn.h"

struct GognNode {
    Gogn data;
    GognNode* next;

    GognNode(string verkefni, bool skolaverkefni, int mikilvaegi){
        data = Gogn(verkefni, skolaverkefni, mikilvaegi);
        next = nullptr;
    }
};