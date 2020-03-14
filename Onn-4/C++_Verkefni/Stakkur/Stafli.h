#pragma once

#include <iostream>
using namespace std;

class Stafli{
    private:
        int staflinn[10];
        int bendill;

    public:
        Stafli();
        void push(int data);
        int pop();
        int peek();
        void prenta();
};