import java.util.*;

public class Solution {

    private static class Task {
        String title;
        boolean done;

        Task(String title) {
            this.title = title;
            this.done = false;
        }
    }

    private static final List<Task> tasks = new ArrayList<>();
    private static final Scanner sc = new Scanner(System.in);

    private static void showTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }
        for (int i = 0; i < tasks.size(); i++) {
            Task t = tasks.get(i);
            System.out.printf("%d. [%s] %s%n", i + 1, t.done ? "✓" : " ", t.title);
        }
    }

    private static void addTask() {
        System.out.print("Task title: ");
        String title = sc.nextLine().trim();
        if (!title.isEmpty()) {
            tasks.add(new Task(title));
            System.out.println("Task added.");
        } else {
            System.out.println("Task title cannot be empty.");
        }
    }

    private static void markComplete() {
        showTasks();
        System.out.print("Task number to mark complete: ");
        try {
            int index = Integer.parseInt(sc.nextLine()) - 1;
            if (index >= 0 && index < tasks.size()) {
                tasks.get(index).done = true;
                System.out.println("Task marked as completed.");
            } else {
                System.out.println("Invalid task number.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input.");
        }
    }

    private static void deleteTask() {
        showTasks();
        System.out.print("Task number to delete: ");
        try {
            int index = Integer.parseInt(sc.nextLine()) - 1;
            if (index >= 0 && index < tasks.size()) {
                tasks.remove(index);
                System.out.println("Task deleted.");
            } else {
                System.out.println("Invalid task number.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input.");
        }
    }

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task Completed");
            System.out.println("4. Delete Task");
            System.out.println("5. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();
            switch (choice) {
                case "1": addTask(); break;
                case "2": showTasks(); break;
                case "3": markComplete(); break;
                case "4": deleteTask(); break;
                case "5": return;
                default: System.out.println("Invalid choice.");
            }
        }
    }
}
