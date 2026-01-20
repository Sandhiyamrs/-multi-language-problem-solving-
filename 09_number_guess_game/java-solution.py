import java.util.Random;
import java.util.Scanner;

public class NumberGuessGame {
    public static void main(String[] args) {

        Random rand = new Random();
        int number = rand.nextInt(100) + 1;

        Scanner sc = new Scanner(System.in);
        System.out.println("Guess a number between 1 and 100");

        while (true) {
            System.out.print("Your guess: ");
            int guess = sc.nextInt();

            if (guess < number) {
                System.out.println("Too Low");
            } else if (guess > number) {
                System.out.println("Too High");
            } else {
                System.out.println("Correct! You guessed the number.");
                break;
            }
        }
        sc.close();
    }
}
