import java.util.*;

public class Solution {

    private static final List<Expense> expenses = new ArrayList<>();

    private static class Expense {
        double amount;
        String category;

        Expense(double amount, String category) {
            this.amount = amount;
            this.category = category;
        }
    }

    private static void addExpense(double amount, String category) {
        expenses.add(new Expense(amount, category));
        System.out.println("Expense added.");
    }

    private static void showTotal() {
        double total = expenses.stream().mapToDouble(e -> e.amount).sum();
        System.out.printf("Total expenses: %.2f%n", total);
    }

    private static void showByCategory() {
        Map<String, Double> map = new HashMap<>();
        for (Expense e : expenses)
            map.put(e.category, map.getOrDefault(e.category, 0.0) + e.amount);

        map.forEach((k, v) ->
                System.out.printf("%s: %.2f%n", k, v));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Expense");
            System.out.println("2. View Total");
            System.out.println("3. View by Category");
            System.out.println("4. Exit");
            System.out.print("Choice: ");
            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    try {
                        System.out.print("Amount: ");
                        double amount = Double.parseDouble(sc.nextLine());
                        System.out.print("Category: ");
                        String category = sc.nextLine();
                        addExpense(amount, category);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount.");
                    }
                    break;
                case "2":
                    showTotal();
                    break;
                case "3":
                    showByCategory();
                    break;
                case "4":
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}

