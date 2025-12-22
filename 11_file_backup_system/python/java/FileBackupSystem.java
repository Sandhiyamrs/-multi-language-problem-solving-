import java.io.*;
import java.nio.file.*;

public class FileBackupSystem {
    public static void main(String[] args) throws IOException {
        Path source = Paths.get("source");
        Path backup = Paths.get("backup");

        if (!Files.exists(source)) {
            System.out.println("Source folder not found");
            return;
        }

        Files.createDirectories(backup);

        DirectoryStream<Path> files = Files.newDirectoryStream(source);
        for (Path file : files) {
            if (Files.isRegularFile(file)) {
                Files.copy(file, backup.resolve(file.getFileName()),
                        StandardCopyOption.REPLACE_EXISTING);
                System.out.println("Backed up: " + file.getFileName());
            }
        }
    }
}
