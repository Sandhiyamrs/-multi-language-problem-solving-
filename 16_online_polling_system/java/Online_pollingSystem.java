import java.util.*;

public class OnlinePollingSystem {
    public static void main(String[] args) {
        String[] candidates = {"Alice", "Bob", "Charlie"};
        int[] votes = new int[candidates.length];
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("Candidates:");
            for (int i = 0; i < candidates.length; i++) {
                System.out.println((i+1) + ". " + candidates[i]);
            }
            System.out.print("Enter candidate number (or 0 to quit): ");
            int choice = sc.nextInt();
            if (choice == 0) break;
            if (choice >= 1 && choice <= candidates.length) votes[choice-1]++;
            else System.out.println("Invalid choice");
        }

        int maxVotes = Arrays.stream(votes).max().getAsInt();
        System.out.print("Winner(s): ");
        for (int i = 0; i < votes.length; i++) {
            if (votes[i] == maxVotes) System.out.print(candidates[i] + " ");
        }
        System.out.println();
    }
}
