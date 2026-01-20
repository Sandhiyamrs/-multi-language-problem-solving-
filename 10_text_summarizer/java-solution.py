import java.util.*;

public class TextSummarizer {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter text:");
        String text = sc.nextLine();

        String[] sentences = text.split("\\.");
        Map<String, Integer> wordFreq = new HashMap<>();

        for (String sentence : sentences) {
            for (String word : sentence.toLowerCase().split(" ")) {
                wordFreq.put(word, wordFreq.getOrDefault(word, 0) + 1);
            }
        }

        Map<String, Integer> sentenceScore = new HashMap<>();

        for (String sentence : sentences) {
            int score = 0;
            for (String word : sentence.toLowerCase().split(" ")) {
                score += wordFreq.getOrDefault(word, 0);
            }
            sentenceScore.put(sentence, score);
        }

        List<String> summary = new ArrayList<>(sentenceScore.keySet());
        summary.sort((a, b) -> sentenceScore.get(b) - sentenceScore.get(a));

        System.out.println("\nSummary:");
        for (int i = 0; i < Math.min(2, summary.size()); i++) {
            System.out.println(summary.get(i).trim() + ".");
        }
        sc.close();
    }
}
