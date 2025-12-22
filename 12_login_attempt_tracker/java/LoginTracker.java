import java.util.Scanner;

public class LoginTracker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int attempts = 0;

        while (attempts < 3) {
            System.out.print("Enter password: ");
            String pwd = sc.nextLine();

            if (pwd.equals("admin123")) {
                System.out.println("Login successful");
                return;
            } else {
                attempts++;
                System.out.println("Wrong password");
            }
        }
        System.out.println("Account locked");
    }
}
