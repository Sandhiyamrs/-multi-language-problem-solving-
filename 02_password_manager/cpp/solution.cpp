#include <iostream>
#include <unordered_map>
#include <openssl/sha.h>
#include <sstream>
#include <iomanip>

using namespace std;

unordered_map<string, string> store;

string hashPassword(const string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)password.c_str(), password.size(), hash);

    stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    return ss.str();
}

void addPassword() {
    string service, password;
    cout << "Service name: ";
    cin >> service;

    if (store.count(service)) {
        cout << "Service already exists.\n";
        return;
    }

    cout << "Password: ";
    cin >> password;
    store[service] = hashPassword(password);
    cout << "Password stored successfully.\n";
}

void retrievePassword() {
    string service;
    cout << "Service name: ";
    cin >> service;

    if (!store.count(service)) {
        cout << "Service not found.\n";
        return;
    }
    cout << "Stored hash: " << store[service] << endl;
}

int main() {
    while (true) {
        cout << "\n1. Add Password\n2. Retrieve Password\n3. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) addPassword();
        else if (choice == 2) retrievePassword();
        else if (choice == 3) break;
        else cout << "Invalid choice\n";
    }
    return 0;
}
