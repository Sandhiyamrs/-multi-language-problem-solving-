#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Student {
    string name;
    double grade;
};

int main() {
    vector<Student> students;

    while (true) {
        cout << "\n1. Add Student\n2. View Students\n3. Show Average\n4. Exit\nChoice: ";
        int choice;
        cin >> choice;

        if (choice == 1) {
            Student s;
            cout << "Student name: ";
            cin >> s.name;
            cout << "Grade: ";
            cin >> s.grade;
            students.push_back(s);
            cout << "Student added.\n";
        }
        else if (choice == 2) {
            if (students.empty())
                cout << "No students available.\n";
            for (auto& s : students)
                cout << s.name << ": " << s.grade << endl;
        }
        else if (choice == 3) {
            if (!students.empty()) {
                double sum = 0;
                for (auto& s : students)
                    sum += s.grade;
                cout << "Class Average: " << sum / students.size() << endl;
            } else {
                cout << "No grades to calculate.\n";
            }
        }
        else if (choice == 4) {
            break;
        }
        else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}
