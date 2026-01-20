#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string source, backup;

    cout << "Enter source file: ";
    cin >> source;

    cout << "Enter backup file: ";
    cin >> backup;

    ifstream in(source, ios::binary);
    ofstream out(backup, ios::binary);

    if (!in) {
        cout << "Source file not found.\n";
        return 0;
    }

    char ch;
    while (in.get(ch)) {
        out.put(ch);
    }

    in.close();
    out.close();

    cout << "Backup created successfully.\n";
    return 0;
}
