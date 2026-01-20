#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int key = 123;
    string inputFile, outputFile;

    cout << "Input file: ";
    cin >> inputFile;
    cout << "Output file: ";
    cin >> outputFile;

    ifstream in(inputFile, ios::binary);
    ofstream out(outputFile, ios::binary);

    char ch;
    while (in.get(ch)) {
        out.put(ch ^ key);
    }

    in.close();
    out.close();

    cout << "File encrypted successfully.\n";
    return 0;
}
