#include <iostream>
#include <vector>
#include <unordered_map>
#include <iomanip>

using namespace std;

struct Expense {
    double amount;
    string category;
};

int main() {
    vector<Expense> expenses;

    while (true) {
        cout << "\n1. Add Expense\n2. View Total\n3. View by Category\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) {
            Expense e;
            cout << "Amount: ";
            cin >> e.amount;
            cout << "Category: ";
            cin >> e.category;
            expenses.push_back(e);
            cout << "Expense added.\n";
        }
        else if (choice == 2) {
            double total = 0;
            for (const auto& e : expenses)
                total += e.amount;
            cout << fixed << setprecision(2)
                 << "Total expenses: " << total << endl;
        }
        else if (choice == 3) {
            unordered_map<string, double> totals;
            for (const auto& e : expenses)
                totals[e.category] += e.amount;

            for (const auto& [cat, total] : totals)
                cout << cat << ": " << fixed << setprecision(2)
                     << total << endl;
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

