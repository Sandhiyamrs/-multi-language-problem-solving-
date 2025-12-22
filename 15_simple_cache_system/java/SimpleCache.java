import java.util.*;

public class SimpleCache {
    public static void main(String[] args) {
        Map<String, String> cache = new HashMap<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("Key (exit to quit): ");
            String key = sc.nextLine();
            if (key.equals("exit")) break;

            System.out.print("Value: ");
            String value = sc.nextLine();
            cache.put(key, value);
            System.out.println(cache);
        }
    }
}
