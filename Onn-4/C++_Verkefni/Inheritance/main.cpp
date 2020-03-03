#include <iostream>

using namespace std;

class A {
    private:
        int tala_a;

    public:
        A() {
            this->tala_a = 0;
            cout << "Default constructor A" << endl;
        }

        A(int t) {
            this->tala_a = t;
            cout << "Hinn constructorinn A" << endl;
        }

        int getATala() { return this->tala_a; }
        virtual void prenta() { cout << "A klasi prenta" << endl; } 

        virtual ~A() {}
};

class B : public A {
    private:
        int tala_b;

    public:
        B() {
            this->tala_b = 0;
            cout << "Default constructor B" << endl;
        }

        B(int a, int b) : A(a) {
            this->tala_b = b;
            cout << "Hinn constructorinn B" << endl;
        }

        void prenta(){
            cout << "B klasi prenta" << endl;
        }
};

class C : public A {
    private:
        int tala_c;

    public:
        C() {
            this->tala_c = 0;
            cout << "Default constructor C" << endl;
        }

        C(int a, int c) : A(a) {
            this->tala_c = c;
            cout << "Hinn constructorinn C" << endl;
        }

        void prenta() {
            cout << "C klasi prenta" << endl;
        }

};

int main(){
    A** as = new A*[2];

    as[0] = new B();
    as[1] = new C();

    as[0]->prenta();
    as[1]->prenta();

    delete as[0];
    delete as[1];
    delete [] as;

    return 0;
}