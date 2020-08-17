#include <iostream>
#include <sstream>

using namespace std;

int main(){

    string inntak;
    string skipun;
    string tegund;
    string nafn;
    string eigandi_matur;
    int id, einkunn;

    do {
        cout << "Hvað viltu gera?: ";
        getline(cin, inntak);
        // inntak => skrá hund 10 snati 7 hundamat
        stringstream ss;
        // ss => skrá hund 10 snati 7 hundamat
        ss << inntak;
        // skipun => skrá
        // ss => hund 10 snati 7 hundamat
        ss >> skipun;
        if(skipun == "skrá"){
            ss >> tegund;
            // ss => 10 snati 7 hundamat
        } else if(skipun == "skoða")  {

        } else if(skipun == "eypa")   {

        } else if(skipun == "breyta") {

        } else if(skipun == "prenta") {

        }
    } while(skipun != "hætta");


    return 0;
};