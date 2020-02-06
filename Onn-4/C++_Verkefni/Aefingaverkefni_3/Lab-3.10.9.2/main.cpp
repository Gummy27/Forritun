#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Collection {
    int elno;
    int *elements;
};


void AddToCollection(Collection &col, int element) {
    // Ef fylkið er col.elements tómt
    if(col.elno == 0){
        // Búa til array-ið elements af stærð 1 á heap
        col.elements = new int[1];
        // Setja element í stak 0 í elements
        col.elements[0] = element;
        // Hækka col.elno um 1
        col.elno++;
    } else { // Annars
        // Búa til temp array af stærð col.elno + 1 á heap
        int* temp = new int[col.elno+1];
        // Afrita stökin í col.elements yfir í temp array-ið
        for(int i = 0; i < col.elno; i++)
            temp[i] = col.elements[i];
        // eyða col.elements
        delete [] col.elements;
        // láta col.elements benda á temp
        col.elements = temp;
        // Setja element í stak col.elno í col.elements
        col.elements[col.elno] = element;
        // Hækka col.elno um einn
        col.elno++;
    }
}

void PrintCollection(Collection col) {
    cout << "[ ";
    for(int i = 0; i < col.elno; i++)
        cout << col.elements[i] << " ";
    cout << "]" << endl;
}

int main(void) {
    Collection collection = { 0, NULL };

    int elems;
    cout << "How many elements? ";
    cin >> elems;
    srand(time(NULL));
    for(int i = 0; i < elems; i++)
        AddToCollection(collection, rand() % 100 + 1);

    PrintCollection(collection);
    delete[] collection.elements;
    return 0;
}