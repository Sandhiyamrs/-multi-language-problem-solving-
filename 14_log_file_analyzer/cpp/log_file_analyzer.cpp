#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream file("app.log");
    string line;
    int count = 0;

    while (getline(file, line)) {
        if (line.find("ERROR") != string::npos)
            count++;
    }
    cout << "Error count: " << count << endl;
}
