import java.io.*;
import java.util.*;

public class SimpleTextEditor {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter filename: ");
        String filename = sc.nextLine();
        System.out.print("Write(w) / Read(r): ");
        String mode = sc.nextLine();

        if (mode.equalsIgnoreCase("w")) {
            BufferedWriter bw = new BufferedWriter(new FileWriter(filename));
            System.out.println("Enter text (type 'END' to finish):");
            while (true) {
                String line = sc.nextLine();
                if (line.equals("END")) break;
                bw.write(line);
                bw.newLine();
            }
            bw.close();
        } else if (mode.equalsIgnoreCase("r")) {
            try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
                String line;
                while ((line = br.readLine()) != null) System.out.println(line);
            } catch (FileNotFoundException e) {
                System.out.println("File not found");
            }
        }
    }
}
