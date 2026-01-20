import java.util.*;

public class Online_pollingSystem {

    public static void main(String[] args) {

        Map<String, Integer> poll = new LinkedHashMap<>();
        poll.put("Option A", 0);
        poll.put("Option B", 0);
        poll.put("Option C", 0);

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Vote");
            System.out.println("2. View Results");
            System.out.println("3. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();

            if (choice.equals("1")) {
                int i = 1;
                for (String option : poll.keySet()) {
                    System.out.println(i + ". " + option);
                    i++;
                }

                System.out.print("Select option number: ");
                int vote = Integer.parseInt(sc.nextLine());
                List<String> options = new ArrayList<>(poll.keySet());

                if (vote >= 1 && vote <= options.size()) {
                    String selected = options.get(vote - 1);
                    poll.put(selected, poll.get(selected) + 1);
                    System.out.println("Vote recorded.");
                } else {
                    System.out.println("Invalid option.");
                }

            } else if (choice.equals("2")) {
                System.out.println("\nResults:");
                for (Map.Entry<String, Integer> entry : poll.entrySet()) {
                    System.out.println(entry.getKey() + " : " + entry.getValue());
                }

            } else if (choice.equals("3")) {
                sc.close();
                return;

            } else {
                System.out.println("Invalid choice.");
            }
        }
    }
}

