import java.io.*;

public class FileEncrypter {
    public static void main(String[] args) throws Exception {

        int key = 123;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Input file: ");
        String inputFile = br.readLine();

        System.out.print("Output file: ");
        String outputFile = br.readLine();

        FileInputStream fis = new FileInputStream(inputFile);
        FileOutputStream fos = new FileOutputStream(outputFile);

        int b;
        while ((b = fis.read()) != -1) {
            fos.write(b ^ key);
        }

        fis.close();
        fos.close();

        System.out.println("File encrypted successfully.");
    }
}
