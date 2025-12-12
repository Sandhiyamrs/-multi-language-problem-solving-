import java.util.*;

public class Solution {
    public static void main(String[] args){
        Random r = new Random();
        int num = r.nextInt(100)+1;
        Scanner sc = new Scanner(System.in);
        int attempts=0, guess;
        do{
            System.out.print("Guess number (1-100): ");
            guess = sc.nextInt(); attempts++;
            if(guess<num) System.out.println("Higher!");
            else if(guess>num) System.out.println("Lower!");
        } while(guess!=num);
        System.out.println("Correct! Attempts: "+attempts);
    }
}
