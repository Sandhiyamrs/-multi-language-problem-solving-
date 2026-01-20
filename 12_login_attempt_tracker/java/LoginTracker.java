import java.util.Scanner;

public class LoginTracker {
    public static void main(String[] args) {

        final String USERNAME = "admin";
        final String PASSWORD = "1234";
        final int MAX_ATTEMPTS = 3;

        Scanner sc = new Scanner(System.in);
        int attempts = 0;

        while (attempts < MAX_ATTEMPTS) {
            System.out.print("Username: ");
            String user = sc.nextLine();

            System.out.print("Password: ");
            String pass = sc.nextLine();

            if (user.equals(USERNAME) && pass.equals(PASSWORD)) {
                System.out.println("Login successful.");
                break;
            } else {
                attempts++;
                System.out.println("Invalid credentials.");
            }
        }

        if (attempts == MAX_ATTEMPTS) {
            System.out.println("Account locked due to too many failed attempts.");
        }
        sc.close();
    }
}
