#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string filename, mode, line;
    cout << "Enter filename: ";
    cin >> filename;
    cout << "Write(w) / Read(r): ";
    cin >> mode;
    cin.ignore();

    if (mode == "w") {
        ofstream file(filename);
        cout << "Enter text (type 'END' to finish):\n";
        while (true) {
            getline(cin, line);
            if (line == "END") break;
            file << line << endl;
        }
    } else if (mode == "r") {
        ifstream file(filename);
        if (!file) { cout << "File not found\n"; return 0; }
        while (getline(file, line)) cout << line << endl;
    }
}
