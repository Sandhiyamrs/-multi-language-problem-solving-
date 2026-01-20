#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Task {
    string title;
    bool done;
};

void showTasks(const vector<Task>& tasks) {
    if (tasks.empty()) {
        cout << "No tasks available.\n";
        return;
    }
    for (size_t i = 0; i < tasks.size(); i++) {
        cout << i + 1 << ". [" << (tasks[i].done ? "✓" : " ") << "] "
             << tasks[i].title << endl;
    }
}

int main() {
    vector<Task> tasks;

    while (true) {
        cout << "\n1. Add Task\n2. View Tasks\n3. Mark Task Completed\n4. Delete Task\n5. Exit\nChoice: ";
        int choice;
        cin >> choice;
        cin.ignore();

        if (choice == 1) {
            Task t;
            cout << "Task title: ";
            getline(cin, t.title);
            t.done = false;
            if (!t.title.empty()) {
                tasks.push_back(t);
                cout << "Task added.\n";
            } else {
                cout << "Task title cannot be empty.\n";
            }
        }
        else if (choice == 2) {
            showTasks(tasks);
        }
        else if (choice == 3) {
            showTasks(tasks);
            cout << "Task number to mark complete: ";
            int idx;
            cin >> idx;
            if (idx >= 1 && idx <= tasks.size()) {
                tasks[idx - 1].done = true;
                cout << "Task marked as completed.\n";
            } else {
                cout << "Invalid task number.\n";
            }
        }
        else if (choice == 4) {
            showTasks(tasks);
            cout << "Task number to delete: ";
            int idx;
            cin >> idx;
            if (idx >= 1 && idx <= tasks.size()) {
                tasks.erase(tasks.begin() + idx - 1);
                cout << "Task deleted.\n";
            } else {
                cout << "Invalid task number.\n";
            }
        }
        else if (choice == 5) {
            break;
        }
        else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}
