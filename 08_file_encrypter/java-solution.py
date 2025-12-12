import java.io.*;
import java.util.Scanner;

public class Solution {
    public static void encryptDecrypt(String path, int key) throws IOException{
        FileInputStream fis = new FileInputStream(path);
        byte[] data = fis.readAllBytes(); fis.close();
        for(int i=0;i<data.length;i++) data[i] ^= key;
        FileOutputStream fos = new FileOutputStream(path+".enc");
        fos.write(data); fos.close();
        System.out.println("File processed!");
    }
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("File path: "); String path = sc.nextLine();
        System.out.print("Enter numeric key: "); int key = sc.nextInt();
        encryptDecrypt(path,key);
    }
}
