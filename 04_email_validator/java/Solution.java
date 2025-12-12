import java.util.regex.*;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter email: ");
        String email = sc.nextLine();
        String regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-z]{2,}$";
        if(Pattern.matches(regex,email)) System.out.println("Valid Email");
        else System.out.println("Invalid Email");
    }
}

