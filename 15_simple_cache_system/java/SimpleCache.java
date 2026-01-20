import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class SimpleCache {
    public static void main(String[] args) {

        Map<String, String> cache = new HashMap<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add to Cache");
            System.out.println("2. Get from Cache");
            System.out.println("3. View Cache");
            System.out.println("4. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Key: ");
                    String key = sc.nextLine();
                    System.out.print("Value: ");
                    String value = sc.nextLine();
                    cache.put(key, value);
                    System.out.println("Stored in cache.");
                    break;

                case "2":
                    System.out.print("Key: ");
                    key = sc.nextLine();
                    System.out.println("Value: " + cache.getOrDefault(key, "Key not found"));
                    break;

                case "3":
                    System.out.println("Cache Contents:");
                    for (Map.Entry<String, String> entry : cache.entrySet()) {
                        System.out.println(entry.getKey() + " : " + entry.getValue());
                    }
                    break;

                case "4":
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
