#include <iostream>
#include <string>

using namespace std;

class Bill{
    private:
        int id;
        string tegund, litur;
    public:
        Bill(){
            this->id = 0;
            this->tegund = "";
            this->litur = "";
        }

        Bill(int id){
            this->id = id;
            this->tegund = "";
            this->litur = "";
        }

        Bill(int id, string tegund, string litur){
            this->id = id;
            this->tegund = tegund;
            this->litur = litur;   
        }

        void prenta(){
            cout << "Id     : " << this->id     << endl
                 << "Tegund : " << this->tegund << endl
                 << "Litur  : " << this->litur  << endl
                 << "-----------------------------------" << endl;
        }

        int getId(){return this->id;} 
        void setId(int id){this->id = id > 0 ? id : this->id;}   

        string getTegund(){return this->tegund;}
        void setTegund(string tegund){this->tegund = tegund;}

        string getLitur(){return this->litur;}
        void setLitur(string litur){this->litur = litur;}
};

int main(){
    Bill bill = Bill(1, "Volvo Sc90", "Grár");
    
    bill.prenta();

    bill.setId(-20);
    bill.prenta();

    bill.setId(1020);
    bill.prenta();

    bill.setTegund("Land Rover Discovery Sport");
    bill.prenta();

    bill.setLitur("Vínrauður");
    bill.prenta();
}