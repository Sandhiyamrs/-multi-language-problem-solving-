import java.util.*;
import java.security.MessageDigest;

public class Solution {

    private static final Map<String, String> store = new HashMap<>();

    private static String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] bytes = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : bytes)
                sb.append(String.format("%02x", b));
            return sb.toString();
        } catch (Exception e) {
            throw new RuntimeException("Hashing failed");
        }
    }

    private static void addPassword(String service, String password) {
        if (store.containsKey(service)) {
            System.out.println("Service already exists.");
            return;
        }
        store.put(service, hashPassword(password));
        System.out.println("Password stored successfully.");
    }

    private static void retrievePassword(String service) {
        if (!store.containsKey(service)) {
            System.out.println("Service not found.");
            return;
        }
        System.out.println("Stored hash: " + store.get(service));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Password");
            System.out.println("2. Retrieve Password");
            System.out.println("3. Exit");
            System.out.print("Choice: ");
            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Service name: ");
                    String service = sc.nextLine();
                    System.out.print("Password: ");
                    String password = sc.nextLine();
                    addPassword(service, password);
                    break;
                case "2":
                    System.out.print("Service name: ");
                    retrievePassword(sc.nextLine());
                    break;
                case "3":
                    return;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
