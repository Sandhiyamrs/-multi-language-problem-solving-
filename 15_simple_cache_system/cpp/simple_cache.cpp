#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    unordered_map<string, string> cache;

    while (true) {
        cout << "\n1. Add to Cache\n2. Get from Cache\n3. View Cache\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) {
            string key, value;
            cout << "Key: ";
            cin >> key;
            cout << "Value: ";
            cin >> value;
            cache[key] = value;
            cout << "Stored in cache.\n";
        }
        else if (choice == 2) {
            string key;
            cout << "Key: ";
            cin >> key;
            if (cache.find(key) != cache.end())
                cout << "Value: " << cache[key] << endl;
            else
                cout << "Key not found.\n";
        }
        else if (choice == 3) {
            cout << "Cache Contents:\n";
            for (auto& pair : cache) {
                cout << pair.first << " : " << pair.second << endl;
            }
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
