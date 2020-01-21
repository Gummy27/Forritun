#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int main() {
    int input;
    int nr;

    while (input != 0){
        cout << "1 - Breyta í tvíundakerfið" << endl
             << "2 - Breyta í áttundakerfið" << endl
             << "3 - Breyta í sextánakerfið" << endl
             << "0 - Hætta"                  << endl
             << "--------------------------" << endl
             << "Veldu aðgerd: ";
        cin >> input;

        switch(input) {
            case 0:
                cout << "Bæ, bæ :(" << endl;
                break;

            case 1 :
                cout << "Sláðu inn tugakerfistölu: ";
                cin >> nr;
                cout << bitset<32>(nr) << endl;
                break;
            
            case 2 :
                cout << "Sláðu inn tugakerfistölu: ";
                cin >> nr;
                cout << oct << nr << dec << endl;
                break;
            
            case 3 :
                cout << "Sláðu inn tugakerfistölu: ";
                cin >> nr;
                cout << hex << nr << dec << endl;
                break;

            default :
                cout << "Þarna skrifaðiru eitthvað vitlaust, reyndu aftur" << endl;
        }
    }
}
