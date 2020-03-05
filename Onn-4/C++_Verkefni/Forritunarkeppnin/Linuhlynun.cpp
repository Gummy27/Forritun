#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    int hus[n][2];
    for(int i = 0; i < n; i++){
        cin >> hus[i][0] >> hus[i][1];
    }

    int co2 = 0;
    int minnsta_eydslan;
    cout << min(hus);
}