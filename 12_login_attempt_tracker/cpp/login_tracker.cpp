#include <iostream>
using namespace std;

int main() {
    int attempts = 0;
    string pwd;

    while (attempts < 3) {
        cout << "Enter password: ";
        cin >> pwd;

        if (pwd == "admin123") {
            cout << "Login successful\n";
            return 0;
        } else {
            attempts++;
            cout << "Wrong password\n";
        }
    }
    cout << "Account locked\n";
}
