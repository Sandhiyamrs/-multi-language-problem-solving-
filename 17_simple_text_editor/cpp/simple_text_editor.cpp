#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<string> text;

    while (true) {
        cout << "\n1. Add Text\n2. View Text\n3. Clear Text\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;
        cin.ignore();

        if (choice == 1) {
            string line;
            cout << "Enter text: ";
            getline(cin, line);
            text.push_back(line);
        }
        else if (choice == 2) {
            cout << "\nCurrent Text:\n";
            for (auto& line : text)
                cout << line << endl;
        }
        else if (choice == 3) {
            text.clear();
            cout << "Text cleared.\n";
        }
        else if (choice == 4) {
            break;
        }
        else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}

