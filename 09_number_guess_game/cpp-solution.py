#include <bits/stdc++.h>
using namespace std;

int main(){
    srand(time(0));
    int num = rand()%100+1, guess, attempts=0;
    do{
        cout << "Guess number (1-100): "; cin >> guess;
        attempts++;
        if(guess<num) cout << "Higher!\n";
        else if(guess>num) cout << "Lower!\n";
    } while(guess!=num);
    cout << "Correct! Attempts: " << attempts << endl;
    return 0;
}
