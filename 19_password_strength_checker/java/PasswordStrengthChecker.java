import java.util.Scanner;

public class PasswordStrengthChecker {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter password: ");
        String password = sc.nextLine();

        boolean hasUpper = false, hasLower = false, hasDigit = false;

        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isDigit(c)) hasDigit = true;
        }

        int score = 0;
        if (hasUpper) score++;
        if (hasLower) score++;
        if (hasDigit) score++;
        if (password.length() >= 8) score++;

        if (score <= 2)
            System.out.println("Weak Password");
        else if (score == 3)
            System.out.println("Medium Password");
        else
            System.out.println("Strong Password");

        sc.close();
    }
}
