#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int ip2int(int* ipFylki){
    unsigned long long ip_binary;

    ip_binary = ipFylki[0];
    ip_binary = (ip_binary << 16) | ipFylki[1];
    ip_binary = (ip_binary << 16) | ipFylki[2];
    ip_binary = (ip_binary << 16) | ipFylki[3];
    ip_binary<<=32;

    cout << bitset<32>(ip_binary) << dec << endl; 
    cout << ip_binary << endl;

    return ip_binary;
}

void ip2fylki(int* ipFylki){

}

void synaIpTolu(string texti, int* ipFylki){
    
}

int main(){
    string starting_ip;
    // int bits, subnets;
    int ipFylki[4];
    cout << "Sláðu inn upphafsnet: ";
    cin >> ipFylki[0] >> ipFylki[1] >> ipFylki[2] >> ipFylki[3];

    ip2int(ipFylki);
    /*
    cout << "Fjöldi netbita í upphafsneti: ";
    cin >> bits;
    cout << "Fjöldi neta sem á að skipta upphafsnetinu í: ";
    cin >> subnets;

    */


    return 0;
}