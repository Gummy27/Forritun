#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n, q;

    cin >> n;
    int hnit[n][2] = {};

    for(int i = 0; i < n; i++)
        cin >> hnit[i][0] >> hnit[i][1];

    cin >> q;
    int styrkur[q] = {};

    for(int i = 0; i < q; i++)
        cin >> styrkur[i];

    int teljari, fjarlaegd;
    for(int i = 0; i < q; i++){
        teljari = 0;
        for(int x = 0; x < n; x++){
            fjarlaegd = sqrt(pow(hnit[x][0], 2)+pow(hnit[x][1], 2));
            if(fjarlaegd < styrkur[i]){
                teljari++;
            }
        }
        cout << teljari << endl;
    }

    return 0;
}