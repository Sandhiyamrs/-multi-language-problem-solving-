#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0));
    int number = rand() % 100 + 1;
    int guess;

    cout << "Guess a number between 1 and 100\n";

    while (true) {
        cout << "Your guess: ";
        cin >> guess;

        if (guess < number) {
            cout << "Too Low\n";
        }
        else if (guess > number) {
            cout << "Too High\n";
        }
        else {
            cout << "Correct! You guessed the number.\n";
            break;
        }
    }
    return 0;
}
