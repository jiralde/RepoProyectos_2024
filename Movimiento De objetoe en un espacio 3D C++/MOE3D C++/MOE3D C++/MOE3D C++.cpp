#include <iostream>
using namespace std;

class Employee {
private:
    // Private attribute
    float salary1, salary2;

public:
    // Setter
    void setSalary(float s1,float s2) {
        salary1 = s1;
        salary2 = s2;
    }
    // Getter
    float getSalary1() {
        return salary1;
    }

    float getSalary2() {
        return salary2;
    }
};

int main() {
    float a1;
    float b1;
    cout << "s1:";
    cin >> a1;
    cout << "b1";
    cin >> b1;

    Employee myObj;
    myObj.setSalary(a1,b1);
    cout << myObj.getSalary1() << endl;
    cout;
    cout << myObj.getSalary2();
    return 0;
}