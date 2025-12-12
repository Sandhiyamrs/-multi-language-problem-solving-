#include <bits/stdc++.h>
using namespace std;

string generatePassword(int length){
    if(length < 8) return "";
    string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string lower = "abcdefghijklmnopqrstuvwxyz";
    string digits = "0123456789";
    string symbols = "!@#$%^&*()_+-={}[]|:;<>,.?/";
    string all = upper + lower + digits + symbols;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, all.size()-1);
    string pwd;
    while(true){
        pwd = "";
        for(int i=0;i<length;i++) pwd += all[dis(gen)];
        if(any_of(pwd.begin(),pwd.end(),::islower) &&
           any_of(pwd.begin(),pwd.end(),::isupper) &&
           any_of(pwd.begin(),pwd.end(),::isdigit) &&
           any_of(pwd.begin(),pwd.end(), [&](char c){ return symbols.find(c)!=string::npos; }))
           break;
    }
    return pwd;
}

int main(){
    int num, length;
    cout << "How many passwords to generate? ";
    cin >> num;
    cout << "Password length: ";
    cin >> length;
    vector<string> passwords;
    for(int i=0;i<num;i++) passwords.push_back(generatePassword(length));
    for(int i=0;i<num;i++) cout << i+1 << ": " << passwords[i] << endl;

    char save;
    cout << "Save passwords to file? (y/n): ";
    cin >> save;
    if(save=='y'){
        ofstream out("passwords.txt");
        for(auto &p: passwords) out << p << endl;
        out.close();
        cout << "Saved to passwords.txt" << endl;
    }
    return 0;
}

