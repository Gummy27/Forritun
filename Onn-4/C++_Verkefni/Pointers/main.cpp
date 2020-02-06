#include <iostream>

using namespace std;

int leggjaSaman(int a, int b) {
    return a + b;
}

void leggjaTiuVidTiu(int* fylki, int staerd) {
    for(int i = 0; i < staerd; i++) {
        fylki[i] += 10;
    }
}

void leggjaSamanFimm(int& a) {
    a += 5;int vector[] = { 3, -5, 7, 10, -4, 14, 5, 2, -13 };
int n = sizeof(vector) / sizeof(vector[0]);
}

int main(){
    int x = 10, y = 20;
    int f[] = {1, 2, 3, 4, 5};
    int k = 20;

    leggjaSamanFimm(k);

    leggjaTiuVidTiu(f, 5);
    cout << f[0] << endl;

    cout << leggjaSaman(x, y) << endl;

    return 0;
}