#pragma once

#include "safnkostir.h"

struct DyrNode {
    safnkostir* dyr; // Gogn data,  int data
    DyrNode* next;
    DyrNode() {
        this->dyr = nullptr;
        this->next = nullptr;
    }
    DyrNode(safnkostir* nyttDyr) {
        this->dyr = nyttDyr;
        this->next = nullptr;
    }
};