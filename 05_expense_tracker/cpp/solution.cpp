#include <bits/stdc++.h>
using namespace std;

struct Expense{
    double amt; string cat, desc;
};

int main(){
    vector<Expense> expenses;
    while(true){
        double amt; cout << "Enter amount (0 to stop): ";
        cin >> amt; cin.ignore();
        if(amt==0) break;
        string cat, desc;
        cout << "Category: "; getline(cin, cat);
        cout << "Description: "; getline(cin, desc);
        expenses.push_back({amt,cat,desc});
    }

    map<string,double> summary;
    for(auto &e: expenses) summary[e.cat]+=e.amt;

    cout << "\nExpense Summary:\n";
    for(auto &p: summary) cout << p.first << ": " << p.second << endl;

    char save; cout << "Export to CSV? (y/n): "; cin >> save;
    if(save=='y'){
        ofstream out("expenses.csv");
        out << "amount,category,desc\n";
        for(auto &e: expenses) out << e.amt << "," << e.cat << "," << e.desc << "\n";
        out.close(); cout << "Saved to expenses.csv\n";
    }
    return 0;
}

