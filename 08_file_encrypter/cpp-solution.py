#include <bits/stdc++.h>
using namespace std;
#include <fstream>

void encrypt_decrypt(string path, int key){
    ifstream in(path, ios::binary);
    vector<char> data((istreambuf_iterator<char>(in)), {});
    in.close();
    for(char &c: data) c ^= key;
    ofstream out(path+".enc", ios::binary);
    out.write(data.data(), data.size());
    out.close();
    cout << "File processed!\n";
}

int main(){
    string file; int key;
    cout << "File path: "; cin >> file;
    cout << "Key: "; cin >> key;
    encrypt_decrypt(file,key);
    return 0;
}
