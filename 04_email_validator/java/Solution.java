import java.util.Scanner;
import java.util.regex.Pattern;

public class Solution {

    private static final String EMAIL_REGEX =
            "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";

    private static boolean isValidEmail(String email) {
        return Pattern.matches(EMAIL_REGEX, email);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter email address: ");
        String email = sc.nextLine().trim();

        if (isValidEmail(email))
            System.out.println("Valid email address.");
        else
            System.out.println("Invalid email address.");
    }
}
