#include <iostream>
using namespace std;


int main(){
    int matrix[10][10] = { };
    int* matrix_ptr = matrix[0];

    for(int x = 1; x <= 10; x++){
        for(int y = x, teljari = 0; teljari < 10; teljari++, y+=x){
            *matrix_ptr = y;
            matrix_ptr += 1;
        }
    }
    
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            cout.width(4);
            cout << matrix[i][j];
        }
        cout << endl;
    }

    return 0;
}