#pragma once

#include <iostream>
#include <string>
#include "Afangi.h"

using namespace std;

class Nemandi {
    private:
        int id;
        string name;
        int size = 2;
        Afangi* afangar = new Afangi[2];

    public:
        Nemandi(int id);
        Nemandi(int id, string name);

        int get_id();
        void set_id(int id);

        string get_name();
        void set_name(string name);

        void skra_afanga(int id, string name, double einkunn);
        void add_space();
        void get_afangar();


        int empty_in_array();

};