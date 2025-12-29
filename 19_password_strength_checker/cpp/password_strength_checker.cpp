#include <iostream>
#include <regex>
using namespace std;

int main() {
    string pwd;
    cout << "Enter password: ";
    cin >> pwd;

    string strength = "Weak";
    if (pwd.length() >= 8 &&
        regex_search(pwd, regex("[A-Z]")) &&
        regex_search(pwd, regex("[a-z]")) &&
        regex_search(pwd, regex("[0-9]")) &&
        regex_search(pwd, regex("[@#$%^&+=]")))
        strength = "Strong";
    else if (pwd.length() >= 6) strength = "Medium";

    cout << "Password strength: " << strength << endl;
}
