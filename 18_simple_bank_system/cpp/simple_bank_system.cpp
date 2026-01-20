#include <iostream>

using namespace std;

int main() {
    double balance = 0.0;

    while (true) {
        cout << "\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) {
            cout << "Balance: " << balance << endl;
        }
        else if (choice == 2) {
            double amount;
            cout << "Enter amount: ";
            cin >> amount;
            balance += amount;
            cout << "Amount deposited.\n";
        }
        else if (choice == 3) {
            double amount;
            cout << "Enter amount: ";
            cin >> amount;
            if (amount <= balance) {
                balance -= amount;
                cout << "Amount withdrawn.\n";
            } else {
                cout << "Insufficient balance.\n";
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
