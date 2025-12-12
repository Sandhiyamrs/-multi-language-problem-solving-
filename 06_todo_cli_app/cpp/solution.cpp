#include <bits/stdc++.h>
using namespace std;

struct Task{ string task; bool done; };
vector<Task> tasks;
string file="tasks.txt";

void load(){
    ifstream in(file);
    string line;
    while(getline(in,line)){
        size_t sep=line.find('|');
        tasks.push_back({line.substr(0,sep), line[sep+1]=='1'});
    }
}
void save(){
    ofstream out(file);
    for(auto &t: tasks) out << t.task << "|" << (t.done?1:0) << "\n";
}

int main(){
    load();
    while(true){
        cout << "\n1.Add 2.Remove 3.Complete 4.Show 5.Exit\nChoice: ";
        int ch; cin >> ch; cin.ignore();
        if(ch==1){ string t; cout<<"Task: "; getline(cin,t); tasks.push_back({t,false}); }
        else if(ch==2){ int i; cout<<"Index: "; cin>>i; if(i>=0 && i<tasks.size()) tasks.erase(tasks.begin()+i);}
        else if(ch==3){ int i; cout<<"Index: "; cin>>i; if(i>=0 && i<tasks.size()) tasks[i].done=true;}
        else if(ch==4){ for(int i=0;i<tasks.size();i++) cout<<i<<": "<<tasks[i].task<<" ["<<(tasks[i].done?"Done":"Pending")<<"]\n";}
        else break;
    }
    save(); cout<<"Tasks saved!\n";
    return 0;
}
