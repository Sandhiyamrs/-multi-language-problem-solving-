#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<string, int> poll;
    poll["Option A"] = 0;
    poll["Option B"] = 0;
    poll["Option C"] = 0;

    while (true) {
        cout << "\n1. Vote\n2. View Results\n3. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) {
            int i = 1;
            for (auto& p : poll) {
                cout << i << ". " << p.first << endl;
                i++;
            }

            cout << "Select option number: ";
            int vote;
            cin >> vote;

            if (vote >= 1 && vote <= poll.size()) {
                auto it = poll.begin();
                advance(it, vote - 1);
                it->second++;
                cout << "Vote recorded.\n";
            } else {
                cout << "Invalid option.\n";
            }
        }
        else if (choice == 2) {
            cout << "\nResults:\n";
            for (auto& p : poll) {
                cout << p.first << " : " << p.second << endl;
            }
        }
        else if (choice == 3) {
            break;
        }
        else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}

