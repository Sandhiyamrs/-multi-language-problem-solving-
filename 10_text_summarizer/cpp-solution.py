#include <bits/stdc++.h>
using namespace std;
#include <regex>

int main(){
    cout << "Enter text: ";
    string text, line;
    getline(cin, text);

    regex word_regex("\\w+");
    map<string,int> freq;
    auto words_begin = sregex_iterator(text.begin(), text.end(), word_regex);
    auto words_end = sregex_iterator();
    for(auto i=words_begin;i!=words_end;++i){
        string w=i->str();
        transform(w.begin(), w.end(), w.begin(), ::tolower);
        freq[w]++;
    }

    vector<pair<string,int>> sorted_words(freq.begin(), freq.end());
    sort(sorted_words.begin(), sorted_words.end(), [](auto &a, auto &b){ return b.second<a.second?false:b.second<a.second?true:b.second>b.second; });
    cout << "Top keywords: ";
    for(int i=0;i<min(5,(int)sorted_words.size());i++) cout << sorted_words[i].first << " ";
    cout << endl;

    regex sentence_regex("([^.!?]+[.!?])");
    vector<pair<string,int>> sentences;
    auto s_begin = sregex_iterator(text.begin(), text.end(), sentence_regex);
    for(auto i=s_begin; i!=sregex_iterator(); ++i){
        string s = i->str();
        int score=0;
        auto w_begin = sregex_iterator(s.begin(), s.end(), word_regex);
        for(auto w_i=w_begin; w_i!=sregex_iterator(); ++w_i){
            string w=w_i->str(); transform(w.begin(), w.end(), w.begin(), ::tolower);
            score+=freq[w];
        }
        sentences.push_back({s,score});
    }
    sort(sentences.begin(), sentences.end(), [](auto &a, auto &b){ return b.second<a.second; });
    cout << "\nSummary:\n";
    for(int i=0;i<min(3,(int)sentences.size());i++) cout << sentences[i].first << endl;
    return 0;
}
