import java.util.ArrayList;
import java.util.Scanner;

public class simpleTextEditor {
    public static void main(String[] args) {

        ArrayList<String> text = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Text");
            System.out.println("2. View Text");
            System.out.println("3. Clear Text");
            System.out.println("4. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Enter text: ");
                    text.add(sc.nextLine());
                    break;

                case "2":
                    System.out.println("\nCurrent Text:");
                    for (String line : text)
                        System.out.println(line);
                    break;

                case "3":
                    text.clear();
                    System.out.println("Text cleared.");
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

