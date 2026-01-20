import java.util.Scanner;

public class SimpleBankSystem {
    public static void main(String[] args) {

        double balance = 0.0;
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.println("Balance: " + balance);
                    break;

                case "2":
                    System.out.print("Enter amount: ");
                    balance += Double.parseDouble(sc.nextLine());
                    System.out.println("Amount deposited.");
                    break;

                case "3":
                    System.out.print("Enter amount: ");
                    double amount = Double.parseDouble(sc.nextLine());
                    if (amount <= balance) {
                        balance -= amount;
                        System.out.println("Amount withdrawn.");
                    } else {
                        System.out.println("Insufficient balance.");
                    }
                    break;

                case "4":
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}

