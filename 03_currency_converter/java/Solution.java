import java.util.*;

public class Solution {

    private static final Map<String, Double> RATES = Map.of(
        "USD", 1.0,
        "EUR", 0.92,
        "INR", 83.0,
        "GBP", 0.79,
        "JPY", 144.0
    );

    private static double convert(double amount, String from, String to) {
        return (amount / RATES.get(from)) * RATES.get(to);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Available currencies: " + RATES.keySet());
        try {
            System.out.print("Enter amount: ");
            double amount = Double.parseDouble(sc.nextLine());

            System.out.print("From currency: ");
            String from = sc.nextLine().toUpperCase();

            System.out.print("To currency: ");
            String to = sc.nextLine().toUpperCase();

            if (!RATES.containsKey(from) || !RATES.containsKey(to)) {
                System.out.println("Unsupported currency.");
                return;
            }

            double result = convert(amount, from, to);
            System.out.printf("%.2f %s = %.2f %s%n", amount, from, result, to);

        } catch (NumberFormatException e) {
            System.out.println("Invalid amount entered.");
        }
    }
}

