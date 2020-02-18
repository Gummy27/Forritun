#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Nemandi{
    private:
        int nr;
        string name;
        double einkunn;
    
    public:
        Nemandi(){
            this->name    = "";
            this->nr      = 0;
            this->einkunn = 0.0;
        }

        Nemandi(string name, int nr){
            this->name    = name;
            this->nr      = nr;
            this->einkunn = 0.0;
        }

        Nemandi(string name, int nr, double einkunn){
            this->name    = name;
            this->nr      = nr;
            this->einkunn = einkunn;
        }

        // Name
        string getName(){ return this->name; }
        void setName(string name){ this->name=name;}

        int getNr(){ return this->nr; }
        void setNr(int nr){ this->nr = nr; }

        double getEinkunn(){ return this->einkunn; }
        void setEinkunn(double einkunn){ this->einkunn = einkunn; }

        void prenta(){
            double einkunn = round( this->einkunn * 100.0 ) / 100.0;
            cout << "Nemandi Númer: " << this->nr   << endl
                 << "Nafn         : " << this->name << endl
                 << "Einkunn      : " << einkunn    << endl
                 << "--------------------------"    << endl;
                
        }
        
};

int main(){
    Nemandi nemendur[5] = {};
    nemendur[0] = Nemandi("John Doe", 1, 4.5);
    nemendur[1] = Nemandi("Gary Dude", 1234, 9.421321421);
    nemendur[2] = Nemandi("Anne Franklin", 2, 6.2132152);
    nemendur[3] = Nemandi("Gunther White", 4, 2.21);
    nemendur[4] = Nemandi("Marilyn Johnson", 8, 6.213);

    for(int i = 0; i < 5; i++){
        nemendur[i].prenta();
    }
}