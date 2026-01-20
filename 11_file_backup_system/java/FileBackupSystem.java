import java.io.*;

public class FileBackupSystem {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter source file: ");
        String source = br.readLine();

        System.out.print("Enter backup file: ");
        String backup = br.readLine();

        FileInputStream fis = new FileInputStream(source);
        FileOutputStream fos = new FileOutputStream(backup);

        int b;
        while ((b = fis.read()) != -1) {
            fos.write(b);
        }

        fis.close();
        fos.close();

        System.out.println("Backup created successfully.");
    }
}
