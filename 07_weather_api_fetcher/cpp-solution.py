#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    string apiKey = "YOUR_API_KEY";
    string city;

    cout << "Enter city name: ";
    cin >> city;

    string command =
        "curl \"https://api.openweathermap.org/data/2.5/weather?q=" +
        city + "&appid=" + apiKey + "&units=metric\"";

    system(command.c_str());

    return 0;
}
