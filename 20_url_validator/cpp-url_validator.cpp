#include <iostream>
#include <regex>
using namespace std;

int main() {
    string url;
    cout << "Enter URL: ";
    cin >> url;

    regex pattern("^(https?://)?(www\\.)?[a-zA-Z0-9-]+\\.[a-z]{2,}(/.*)?$");
    cout << (regex_match(url, pattern) ? "Valid URL" : "Invalid URL") << endl;
}
