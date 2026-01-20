#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    string filename;
    cout << "Enter log file name: ";
    cin >> filename;

    ifstream file(filename);
    if (!file) {
        cout << "Log file not found.\n";
        return 0;
    }

    int error = 0, warning = 0, info = 0;
    string line;

    while (getline(file, line)) {
        if (line.find("ERROR") != string::npos)
            error++;
        else if (line.find("WARNING") != string::npos)
            warning++;
        else if (line.find("INFO") != string::npos)
            info++;
    }

    file.close();

    cout << "\nLog Summary:\n";
    cout << "ERROR: " << error << endl;
    cout << "WARNING: " << warning << endl;
    cout << "INFO: " << info << endl;

    return 0;
}
