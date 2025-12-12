import java.util.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter text:");
        String text = sc.nextLine();
        Map<String,Integer> freq = new HashMap<>();
        for(String w:text.toLowerCase().split("\\W+")) freq.put(w,freq.getOrDefault(w,0)+1);
        List<Map.Entry<String,Integer>> list = new ArrayList<>(freq.entrySet());
        list.sort((a,b)->b.getValue()-a.getValue());
        System.out.print("Top keywords: ");
        for(int i=0;i<Math.min(5,list.size());i++) System.out.print(list.get(i).getKey()+" ");
        System.out.println();

        String[] sentences = text.split("(?<=[.!?])\\s+");
        List<String[]> scored = new ArrayList<>();
        for(String s: sentences){
            int score=0;
            for(String w: s.toLowerCase().split("\\W+")) score+=freq.getOrDefault(w,0);
            scored.add(new String[]{s,String.valueOf(score)});
        }
        scored.sort((a,b)->Integer.parseInt(b[1])-Integer.parseInt(a[1]));
        System.out.println("\nSummary:");
        for(int i=0;i<Math.min(3,scored.size());i++) System.out.println(scored.get(i)[0]);
    }
}
