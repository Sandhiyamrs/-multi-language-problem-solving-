import java.util.*;
import java.io.*;

class Expense {
    double amount; String category, desc;
    Expense(double a,String c,String d){ amount=a; category=c; desc=d;}
}

public class Solution {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        List<Expense> expenses = new ArrayList<>();
        while(true){
            System.out.print("Enter amount (0 to stop): ");
            double amt = sc.nextDouble(); sc.nextLine();
            if(amt==0) break;
            System.out.print("Category: "); String cat = sc.nextLine();
            System.out.print("Description: "); String desc = sc.nextLine();
            expenses.add(new Expense(amt,cat,desc));
        }

        Map<String, Double> summary = new HashMap<>();
        for(Expense e: expenses) summary.put(e.category, summary.getOrDefault(e.category,0.0)+e.amount);
        System.out.println("\nExpense Summary:");
        for(String k: summary.keySet()) System.out.println(k+": "+summary.get(k));

        System.out.print("Export to CSV? (y/n): ");
        char save = sc.next().charAt(0);
        if(save=='y'){
            PrintWriter pw = new PrintWriter("expenses.csv");
            pw.println("amount,category,desc");
            for(Expense e: expenses) pw.println(e.amount+","+e.category+","+e.desc);
            pw.close();
            System.out.println("Saved to expenses.csv");
        }
    }
}

