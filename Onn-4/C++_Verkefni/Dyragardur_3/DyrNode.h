#pragma once

#include "Dyr.h"

struct DyrNode {
    Dyr* dyr; // Gogn data,  int data
    DyrNode* next;
    DyrNode() {
        this->dyr = nullptr;
        this->next = nullptr;
    }
    DyrNode(Dyr* nyttDyr) {
        this->dyr = nyttDyr;
        this->next = nullptr;
    }
};