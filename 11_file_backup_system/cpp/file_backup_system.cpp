#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    fs::path source = "source";
    fs::path backup = "backup";

    if (!fs::exists(source)) {
        std::cout << "Source folder not found\n";
        return 0;
    }

    fs::create_directories(backup);

    for (auto& file : fs::directory_iterator(source)) {
        if (fs::is_regular_file(file)) {
            fs::copy(file.path(), backup / file.path().filename(),
                     fs::copy_options::overwrite_existing);
            std::cout << "Backed up: " << file.path().filename() << "\n";
        }
    }
}
