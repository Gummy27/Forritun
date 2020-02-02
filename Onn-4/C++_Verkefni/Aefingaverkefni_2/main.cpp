#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int gettingInput(){
    int value;

    cout << "1. Hástafir eða lágstafir með bitaðgerðum" << endl
         << "2. Subnetting með ip tölum"                << endl
         << "0. Hætta"                                  << endl
         << "Hvaða verkefni viltu skoða? : ";
    cin >> value;

    return value;
}

void iLagstafi(string texti){
    char temp;
    string newString = "";
    for(unsigned long i = 0; i < texti.length(); i++){
        temp = texti[i] | 32;
        newString.push_back(temp);
    }
    cout << newString << endl;
}

void iHastafi(string texti){
    char temp;
    string newString = "";
    for(unsigned long i = 0; i < texti.length(); i++){
        if(texti[i] != ' '){
            temp = texti[i] ^ 32;
            newString.push_back(temp);
        } else {
            newString.push_back(texti[i]);
        }
    }
    cout << newString << endl;
}

void vixlad(string texti){
    char temp;
    string newString = "";
    for(unsigned long i = 0; i < texti.length(); i++){
        if(texti[i] != ' '){
            temp = ~((~texti[i]) ^ 32);
            newString.push_back(temp);
        } else {
            newString.push_back(texti[i]);
        }
    }
    cout << newString << endl;
}

unsigned ip2int(long* fylki){
    unsigned long binary = 0;

    fylki[0] <<= 24;
    fylki[1] <<= 16;
    fylki[2] <<= 8;

    binary = fylki[0] | fylki[1] | fylki[2] | fylki[3];
    return binary;
}

void ip2Fylki(int* ipFylki, unsigned long ipTala){
    // unsigned long temp;

    ipFylki[0] = ipTala >> 24;
    ipFylki[1] = ipTala >> 16;
    

    /*
    for(int i = 0; i < 4; i++){
        temp = ipTala >> 24;
        ipFylki[i] = temp;
        ipTala <<= 8;
        cout << bitset<32>(temp) << endl;
    }
    */
}

int main() {
    long input[4] = {192, 168, 1, 0};
    // cin >> input[0] >> input[1] >> input[2] >> input[3];

    unsigned long ip = ip2int(input);
    int ipFylki[4] = {0, 0, 0, 0};

    ip2Fylki(ipFylki, ip);

    cout << ipFylki[0] << endl
         << ipFylki[1] << endl
         << ipFylki[2] << endl
         << ipFylki[3] << endl;

    // cout << bitset<32>(ipFylki[0]);
    /*
    iLagstafi("OK THIS IS KINDA EPIC");
    iHastafi("oK this is kinda epic");
    vixlad("Ok ThIs Is KiNdA ePiC");

    int input = gettingInput();
    while(input){
        
        if(input == 1){
            

        } else if(input == 2){

        } else {
            cout << "Þetta er ekki verkefni, reyndu aftur."
        }

        input = gettingInput();
    }

    cout << "Sjáumst seinna." << endl;    
    */
}
