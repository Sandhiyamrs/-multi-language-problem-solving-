import java.util.regex.*;
import java.util.Scanner;

public class PasswordStrengthChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter password: ");
        String pwd = sc.nextLine();
        String strength = "Weak";

        if (pwd.length() >= 8 &&
            Pattern.compile("[A-Z]").matcher(pwd).find() &&
            Pattern.compile("[a-z]").matcher(pwd).find() &&
            Pattern.compile("[0-9]").matcher(pwd).find() &&
            Pattern.compile("[@#$%^&+=]").matcher(pwd).find())
            strength = "Strong";
        else if (pwd.length() >= 6) strength = "Medium";

        System.out.println("Password strength: " + strength);
    }
}
