#include <iostream>
using namespace std;

int main() {
    int marks[5], sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> marks[i];
        sum += marks[i];
    }
    double avg = sum / 5.0;
    cout << "Average: " << avg << endl;
}
