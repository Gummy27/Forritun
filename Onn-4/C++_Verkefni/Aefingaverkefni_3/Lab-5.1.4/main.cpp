#include <iostream>
#include <string>

using namespace std;

class ShoptItemOrder {
    private:
        string name;
        int price;
        int ordered;

    public:

        ShoptItemOrder() {
            this->name = "";
            this->price = 0;
            this->ordered = 0;
        }

        ShoptItemOrder(string name, int price, int ordered) {
            this->name = name;
            this-> price = price;
            this->ordered = ordered;
        }

        string getName(){ return name;}
        void setName(string name) { this->name = name;}

        int getPrice(){ return price; }
        void setPrice(int price) {this->price = price;}

        int getOrdered(){ return ordered; }
        void setOrdered(int ordered){ this->ordered = ordered;}

        int totalPrice(){
            return this->price * this->ordered;
        }

        void prenta(){
            cout << "Vara: " << this->name    << endl
                 << "Verð: " << this->price   << " kr." << endl
                 << "Magn: " << this->ordered << endl
                 << "---------------------"   << endl;
        }
        
};

int main(){
    ShoptItemOrder klassi = ShoptItemOrder("Skór", 1000, 4);

    klassi.prenta();

    klassi.setName("Úlpa");
    klassi.prenta();

    klassi.setPrice(3000);
    klassi.prenta();

    klassi.setOrdered(10);
    klassi.prenta();

    return 0;
}