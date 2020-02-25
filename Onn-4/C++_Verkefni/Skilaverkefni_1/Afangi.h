#pragma once

#include <iostream>
#include <string>

using namespace std;

class Afangi {
    private: 
        int id;
        string name;
        double einkunn;

    public:
        Afangi();
        Afangi(int id, string name, double einkunn);

        int get_id();
        void set_id(int id);

        string get_name();
        void set_name(string name);

        double get_einkunn();
        void set_einkunn(double einkunn);


};