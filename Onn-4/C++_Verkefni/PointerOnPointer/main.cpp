#include <iostream>

using namespace std;

class A {
  public:
    virtual void prenta() { cout << "Þetta er A klasinn!" << endl; }
    ~A() {}
};

class B : public A {
  public:
    void prenta() { cout << "Þetta er B klasinn!" << endl; }
};

class C : public A {
  public:
    void prenta() { cout << "Þetta er C klasinn!" << endl; }  
};

class AListi {
    private:
        A** listinn;
        int fjoldi;
        int staerd;

    public:
        AListi(){
            this->staerd = 2;
            this->listinn = new A*[this->staerd];
            this->fjoldi = 0;
        }

        void SkraILista(A* item){
            if(this->fjoldi < this->staerd) {
                this->listinn[fjoldi++] = item;
            } else {
                A** temp = new A*[this->staerd+2];
                for(int i = 0; i < this->staerd; i++){
                    temp[i] = this->listinn[i];
                }
                delete [] this->listinn;
                this->listinn = temp;
                this->staerd += 2;
                this->listinn[fjoldi++] = item;
            }
        }

        void prentaLista(){
            for(int i = 0; i < this->fjoldi; i++){
                this->listinn[i]->prenta(); 
            }
        }
        ~AListi(){
            for(int i = 0; i < this->fjoldi; i++){
                delete this->listinn[i];
            }
            delete [] this->listinn;
        }
};

int main(){
    AListi listi;
    listi.SkraILista(new B());
    listi.SkraILista(new C());
    listi.SkraILista(new B());
    listi.SkraILista(new C());
    listi.SkraILista(new A());

    listi.prentaLista();

    return 0;
}