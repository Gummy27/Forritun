#include <iostream>

using namespace std;

int main(){
    int vector[] = { 3, -5, 7, 10, -4, 14, 5, 2, -13 };
    int n = sizeof(vector) / sizeof(vector[0]);
    int* n_ptr = vector;

    int highest = 0;
    for(int i = 0; i < n; i++){
        if(highest < *(n_ptr+i)){
            highest = *(n_ptr+i);
        }
    }

    cout << highest << endl;
}