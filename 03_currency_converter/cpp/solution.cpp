#include <bits/stdc++.h>
using namespace std;

// Note: C++ cannot directly fetch live API without extra libraries.
// We'll use a static example for demonstration.

int main() {
    double amount; string from, to;
    cout << "Amount: "; cin >> amount;
    cout << "From (USD/EUR/INR/...): "; cin >> from;
    cout << "To (USD/EUR/INR/...): "; cin >> to;

    map<string,double> rates = {{"USD",1},{"EUR",0.92},{"INR",83},{"GBP",0.80}};
    if(rates.count(from) && rates.count(to)){
        double converted = amount / rates[from] * rates[to];
        cout << amount << " " << from << " = " << fixed << setprecision(2) << converted << " " << to << endl;
    } else cout << "Currency not supported.\n";
    return 0;
}
