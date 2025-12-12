#include <bits/stdc++.h>
#include <openssl/md5.h>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

string md5_hash(const string &path) {
    ifstream file(path, ios::binary);
    vector<unsigned char> buffer((istreambuf_iterator<char>(file)), {});
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5(buffer.data(), buffer.size(), result);
    stringstream ss;
    for(int i=0;i<MD5_DIGEST_LENGTH;i++)
        ss << hex << setw(2) << setfill('0') << (int)result[i];
    return ss.str();
}

int main() {
    string folderPath;
    cout << "Enter folder path: ";
    cin >> folderPath;

    map<string, string> seen;
    vector<pair<string,string>> duplicates;
    long long total_size = 0;

    for (auto &p : fs::directory_iterator(folderPath)) {
        if (fs::is_regular_file(p)) {
            string path = p.path().string();
            try {
                string hash = md5_hash(path);
                if(seen.count(hash)) {
                    duplicates.push_back({path, seen[hash]});
                    total_size += fs::file_size(p);
                }
                else seen[hash] = path;
            } catch (...) { continue; }
        }
    }

    if(!duplicates.empty()){
        cout << "Duplicate files found:\n";
        for(auto &d: duplicates) cout << d.first << " == " << d.second << "\n";
        cout << "Total duplicates: " << duplicates.size() << "\n";
        cout << "Total space wasted: " << total_size/1024.0 << " KB\n";
    } else cout << "No duplicates found.\n";

    return 0;
}

