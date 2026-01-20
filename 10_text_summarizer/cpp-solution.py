#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string text;
    cout << "Enter text:\n";
    getline(cin, text);

    stringstream ss(text);
    vector<string> sentences;
    string temp;

    while (getline(ss, temp, '.')) {
        sentences.push_back(temp);
    }

    map<string, int> wordFreq;

    for (auto& s : sentences) {
        stringstream ws(s);
        string word;
        while (ws >> word) {
            wordFreq[word]++;
        }
    }

    vector<pair<int, string>> scores;

    for (auto& s : sentences) {
        int score = 0;
        stringstream ws(s);
        string word;
        while (ws >> word) {
            score += wordFreq[word];
        }
        scores.push_back({score, s});
    }

    sort(scores.rbegin(), scores.rend());

    cout << "\nSummary:\n";
    for (int i = 0; i < min(2, (int)scores.size()); i++) {
        cout << scores[i].second << ".\n";
    }

    return 0;
}
