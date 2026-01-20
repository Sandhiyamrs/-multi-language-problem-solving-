import java.io.*;

public class LogFileAnalyzer {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter log file name: ");
        String filename = br.readLine();

        int error = 0, warning = 0, info = 0;

        BufferedReader file = new BufferedReader(new FileReader(filename));
        String line;

        while ((line = file.readLine()) != null) {
            if (line.contains("ERROR")) error++;
            else if (line.contains("WARNING")) warning++;
            else if (line.contains("INFO")) info++;
        }

        file.close();

        System.out.println("\nLog Summary:");
        System.out.println("ERROR: " + error);
        System.out.println("WARNING: " + warning);
        System.out.println("INFO: " + info);
    }
}
