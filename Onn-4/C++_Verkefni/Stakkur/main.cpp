#include <iostream>
#include "Stafli.h"

int main(){
    Stafli s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(40);
    s.prenta();
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    s.prenta();

    cout << s.peek() << endl;


    return 0;
}