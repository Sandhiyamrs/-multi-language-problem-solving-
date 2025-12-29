#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> candidates = {"Alice", "Bob", "Charlie"};
    vector<int> votes(candidates.size(), 0);
    string input;

    while (true) {
        cout << "Candidates:\n";
        for (int i = 0; i < candidates.size(); i++)
            cout << i+1 << ". " << candidates[i] << endl;

        cout << "Enter candidate number (q to quit): ";
        cin >> input;
        if (input == "q") break;
        int choice = stoi(input);
        if (choice >= 1 && choice <= candidates.size()) votes[choice-1]++;
        else cout << "Invalid choice\n";
    }

    int maxVotes = 0;
    for (int v : votes) if (v > maxVotes) maxVotes = v;

    cout << "Winner(s): ";
    for (int i = 0; i < votes.size(); i++)
        if (votes[i] == maxVotes) cout << candidates[i] << " ";
    cout << endl;
}
