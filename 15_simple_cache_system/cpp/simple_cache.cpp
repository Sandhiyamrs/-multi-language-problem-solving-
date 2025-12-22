#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, string> cache;
    string key, value;

    while (true) {
        cout << "Key (exit to quit): ";
        cin >> key;
        if (key == "exit") break;

        cout << "Value: ";
        cin >> value;
        cache[key] = value;
    }
}
