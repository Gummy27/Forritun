#pragma once

#include <iostream>
#include <string>

using namespace std;

class Klasi {
    private:
        int tala;
        string texti;
    public:
        Klasi();
        Klasi(int tala, string texti);
        
        int gettTala();
        void setTala(int tala);

        string getTexti();
        void setTexti(string texti);

        bool operator>(Klasi& other);
        bool operator<(Klasi& other);

        bool operator>=(Klasi& other);
        bool operator<=(Klasi& other);

        bool operator==(Klasi& other);
        bool operator!=(Klasi& other);
}; 

ostream& operator<<(ostream& ostr, Klasi& k);