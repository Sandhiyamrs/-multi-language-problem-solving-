#include <iostream>
#include <string>

using namespace std;

int main() {
    const string USERNAME = "admin";
    const string PASSWORD = "1234";
    const int MAX_ATTEMPTS = 3;

    int attempts = 0;
    string user, pass;

    while (attempts < MAX_ATTEMPTS) {
        cout << "Username: ";
        cin >> user;

        cout << "Password: ";
        cin >> pass;

        if (user == USERNAME && pass == PASSWORD) {
            cout << "Login successful.\n";
            break;
        } else {
            attempts++;
            cout << "Invalid credentials.\n";
        }
    }

    if (attempts == MAX_ATTEMPTS) {
        cout << "Account locked due to too many failed attempts.\n";
    }

    return 0;
}
