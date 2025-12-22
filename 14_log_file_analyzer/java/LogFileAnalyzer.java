import java.io.*;

public class LogFileAnalyzer {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("app.log"));
        int count = 0;
        String line;

        while ((line = br.readLine()) != null) {
            if (line.contains("ERROR")) count++;
        }
        System.out.println("Error count: " + count);
    }
}
