#include <bits/stdc++.h>
using namespace std;
#include <regex>

int main(){
    string email;
    cout << "Enter email: ";
    cin >> email;
    regex pattern("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-z]{2,}$");
    if(regex_match(email, pattern)) cout << "Valid Email\n";
    else cout << "Invalid Email\n";
    return 0;
}

