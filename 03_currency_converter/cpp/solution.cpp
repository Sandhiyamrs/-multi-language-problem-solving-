#include <iostream>
#include <unordered_map>
#include <iomanip>

using namespace std;

int main() {
    unordered_map<string, double> rates = {
        {"USD", 1.0},
        {"EUR", 0.92},
        {"INR", 83.0},
        {"GBP", 0.79},
        {"JPY", 144.0}
    };

    double amount;
    string from, to;

    cout << "Available currencies: ";
    for (const auto& r : rates)
        cout << r.first << " ";
    cout << endl;

    cout << "Enter amount: ";
    cin >> amount;

    cout << "From currency: ";
    cin >> from;
    cout << "To currency: ";
    cin >> to;

    if (!rates.count(from) || !rates.count(to)) {
        cout << "Unsupported currency.\n";
        return 0;
    }

    double result = (amount / rates[from]) * rates[to];
    cout << fixed << setprecision(2);
    cout << amount << " " << from << " = " << result << " " << to << endl;

    return 0;
}
