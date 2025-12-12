import java.io.*;
import java.nio.file.*;
import java.security.*;
import java.util.*;

public class Solution {
    public static String md5Hash(File file) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] data = Files.readAllBytes(file.toPath());
        md.update(data);
        byte[] hashBytes = md.digest();
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes) sb.append(String.format("%02x", b));
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter folder path: ");
        String folderPath = sc.nextLine();
        File folder = new File(folderPath);

        Map<String, String> seen = new HashMap<>();
        List<String[]> duplicates = new ArrayList<>();
        long totalSize = 0;

        for (File file : folder.listFiles()) {
            if (file.isFile()) {
                try {
                    String hash = md5Hash(file);
                    if (seen.containsKey(hash)) {
                        duplicates.add(new String[]{file.getAbsolutePath(), seen.get(hash)});
                        totalSize += file.length();
                    } else {
                        seen.put(hash, file.getAbsolutePath());
                    }
                } catch (Exception e) { continue; }
            }
        }

        if (!duplicates.isEmpty()) {
            System.out.println("Duplicate files found:");
            for (String[] pair : duplicates) System.out.println(pair[0] + " == " + pair[1]);
            System.out.println("Total duplicates: " + duplicates.size());
            System.out.println("Total space wasted: " + totalSize/1024 + " KB");
        } else {
            System.out.println("No duplicates found.");
        }
    }
}

