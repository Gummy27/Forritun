#include <iostream>

using namespace std;

#include "Leikmadur.h"
#include "VistarLeikmadur.h"
#include "Stada.h"

std::ostream& operator<<(std::ostream& out, VistarLeikmadur f){
    out << f.getAllt();
    return out;
}

int main() {
    Stada austur('A', "Austur");
    Stada vestur('V', "Vestur");

    VistarLeikmadur geir(101, "Geir", 0, austur);
    VistarLeikmadur konni(102, "Konni", 0, vestur);
    
    geir.setStig(10);
    konni.setStig(3);
    geir.getAllt();
    
    cout << geir << endl;
    cout << konni << endl;
    
    if(geir < konni) 
        cout << konni.getNafn() << " vann!\n";
    else 
        cout << geir.getNafn() << " vann!\n";

    return 0;
}