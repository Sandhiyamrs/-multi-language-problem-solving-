import java.util.regex.*;
import java.util.Scanner;

public class URLValidator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter URL: ");
        String url = sc.nextLine();

        String pattern = "^(https?://)?(www\\.)?[a-zA-Z0-9-]+\\.[a-z]{2,}(/.*)?$";
        if (Pattern.matches(pattern, url)) System.out.println("Valid URL");
        else System.out.println("Invalid URL");
    }
}
