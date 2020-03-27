#pragma once

#include "Verkefni.h"

struct GognNode {
    Verkefni data;
    GognNode* next;

    GognNode(string verkefni, bool skolaverkefni, int mikilvaegi){
        data = Verkefni(verkefni, skolaverkefni, mikilvaegi);
        next = nullptr;
    }
};