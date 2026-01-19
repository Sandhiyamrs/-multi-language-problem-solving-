import java.io.*;
import java.nio.file.*;
import java.security.*;
import java.util.*;

public class Solution {

    private static String getFileHash(Path path) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        try (InputStream is = Files.newInputStream(path)) {
            byte[] buffer = new byte[4096];
            int read;
            while ((read = is.read(buffer)) != -1) {
                md.update(buffer, 0, read);
            }
        }
        byte[] hashBytes = md.digest();
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes)
            sb.append(String.format("%02x", b));
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter directory path: ");
        Path dir = Paths.get(sc.nextLine());

        Map<String, List<Path>> fileMap = new HashMap<>();

        try {
            Files.walk(dir)
                 .filter(Files::isRegularFile)
                 .forEach(path -> {
                     try {
                         String hash = getFileHash(path);
                         fileMap.computeIfAbsent(hash, k -> new ArrayList<>()).add(path);
                     } catch (Exception ignored) {}
                 });

            boolean found = false;
            for (List<Path> paths : fileMap.values()) {
                if (paths.size() > 1) {
                    found = true;
                    System.out.println("Duplicate group:");
                    paths.forEach(System.out::println);
                    System.out.println("-------------------------");
                }
            }

            if (!found)
                System.out.println("No duplicate files found.");

        } catch (IOException e) {
            System.out.println("Invalid directory.");
        }
    }
}
