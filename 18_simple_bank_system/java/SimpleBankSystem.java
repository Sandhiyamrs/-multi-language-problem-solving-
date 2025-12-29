import java.util.Scanner;

public class SimpleBankSystem {
    public static void main(String[] args) {
        double balance = 0;
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("1. Deposit 2. Withdraw 3. Balance 4. Exit");
            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Deposit amount: ");
                    balance += sc.nextDouble(); sc.nextLine();
                    break;
                case "2":
                    System.out.print("Withdraw amount: ");
                    double amt = sc.nextDouble(); sc.nextLine();
                    if (amt <= balance) balance -= amt;
                    else System.out.println("Insufficient funds");
                    break;
                case "3":
                    System.out.println("Balance: " + balance);
                    break;
                case "4": return;
                default: System.out.println("Invalid choice");
            }
        }
    }
}
