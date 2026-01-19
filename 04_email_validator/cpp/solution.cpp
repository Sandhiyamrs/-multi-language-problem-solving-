#include <iostream>
#include <regex>

using namespace std;

int main() {
    string email;
    cout << "Enter email address: ";
    cin >> email;

    regex pattern("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

    if (regex_match(email, pattern))
        cout << "Valid email address.\n";
    else
        cout << "Invalid email address.\n";

    return 0;
}

