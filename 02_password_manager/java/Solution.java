import java.util.*;
import java.io.*;

public class Solution {
    public static String generatePassword(int length) {
        if(length < 8) return null;
        String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lower = "abcdefghijklmnopqrstuvwxyz";
        String digits = "0123456789";
        String symbols = "!@#$%^&*()_+-={}[]|:;<>,.?/";
        String all = upper + lower + digits + symbols;
        Random r = new Random();
        String pwd;
        while(true){
            StringBuilder sb = new StringBuilder();
            for(int i=0;i<length;i++)
                sb.append(all.charAt(r.nextInt(all.length())));
            pwd = sb.toString();
            if(pwd.chars().anyMatch(Character::isLowerCase) &&
               pwd.chars().anyMatch(Character::isUpperCase) &&
               pwd.chars().anyMatch(Character::isDigit) &&
               pwd.chars().anyMatch(c -> symbols.indexOf(c)>=0))
                break;
        }
        return pwd;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of passwords to generate: ");
        int num = sc.nextInt();
        System.out.print("Password length: ");
        int length = sc.nextInt();
        List<String> passwords = new ArrayList<>();
        for(int i=0;i<num;i++) passwords.add(generatePassword(length));
        for(int i=0;i<passwords.size();i++) System.out.println((i+1)+": "+passwords.get(i));

        System.out.print("Save passwords to file? (y/n): ");
        char choice = sc.next().charAt(0);
        if(choice == 'y'){
            PrintWriter pw = new PrintWriter("passwords.txt");
            for(String p: passwords) pw.println(p);
            pw.close();
            System.out.println("Saved to passwords.txt");
        }
    }
}

