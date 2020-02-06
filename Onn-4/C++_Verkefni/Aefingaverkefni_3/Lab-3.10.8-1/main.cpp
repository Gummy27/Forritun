#include <iostream>
using namespace std;

int main(){

    int maxball;
    int ballsno;

    cout << "Max ball number? : ";
    cin >> maxball;
    cout << "How many balls? : ";
    cin >> ballsno;
    srand(time(NULL));

    int* used = new int[1];
    int numbers[ballsno];

    for(int i = 0; i < ballsno; i++){
        int rnd = rand() % maxball;

        if(sizeof(*used) > 0){
            int *ptr = used;
            for(int i = 0; i < sizeof(*used); i++){
                if(*ptr == rnd){
                    i -= 1;
                    break;
                }
            }
        } else {
            *used = rnd;
        }

        numbers[i] = rnd;
        //cout << rnd << endl;
    }

    for(int i = 0; i < ballsno; i++){
        cout << numbers[i] << endl;
    }
}