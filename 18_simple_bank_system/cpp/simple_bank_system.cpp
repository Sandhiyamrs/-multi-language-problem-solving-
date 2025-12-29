#include <iostream>
using namespace std;

int main() {
    double balance = 0;
    string choice;
    double amount;

    while (true) {
        cout << "1. Deposit 2. Withdraw 3. Balance 4. Exit\nChoice: ";
        cin >> choice;
        if (choice == "1") { cin >> amount; balance += amount; }
        else if (choice == "2") { cin >> amount; 
            if (amount <= balance) balance -= amount;
            else cout << "Insufficient funds\n";
        }
        else if (choice == "3") cout << "Balance: " << balance << endl;
        else if (choice == "4") break;
        else cout << "Invalid choice\n";
    }
}
