#include <iostream>
#include <filesystem>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <iomanip>
#include <openssl/md5.h>

namespace fs = std::filesystem;
using namespace std;

string getFileHash(const fs::path& path) {
    ifstream file(path, ios::binary);
    MD5_CTX ctx;
    MD5_Init(&ctx);

    char buffer[4096];
    while (file.read(buffer, sizeof(buffer)))
        MD5_Update(&ctx, buffer, file.gcount());
    MD5_Update(&ctx, buffer, file.gcount());

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5_Final(result, &ctx);

    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
        ss << hex << setw(2) << setfill('0') << (int)result[i];
    return ss.str();
}

int main() {
    string dirPath;
    cout << "Enter directory path: ";
    cin >> dirPath;

    unordered_map<string, vector<fs::path>> fileMap;

    for (const auto& entry : fs::recursive_directory_iterator(dirPath)) {
        if (fs::is_regular_file(entry)) {
            try {
                string hash = getFileHash(entry.path());
                fileMap[hash].push_back(entry.path());
            } catch (...) {}
        }
    }

    bool found = false;
    for (const auto& [hash, files] : fileMap) {
        if (files.size() > 1) {
            found = true;
            cout << "Duplicate group:\n";
            for (const auto& file : files)
                cout << file << endl;
            cout << "----------------------\n";
        }
    }

    if (!found)
        cout << "No duplicate files found.\n";

    return 0;
}
