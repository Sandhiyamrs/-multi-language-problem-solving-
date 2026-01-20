import java.util.*;

public class StudentGradeManager {

    static class Student {
        String name;
        double grade;

        Student(String name, double grade) {
            this.name = name;
            this.grade = grade;
        }
    }

    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Student");
            System.out.println("2. View Students");
            System.out.println("3. Show Average");
            System.out.println("4. Exit");
            System.out.print("Choice: ");

            String choice = sc.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Student name: ");
                    String name = sc.nextLine();
                    System.out.print("Grade: ");
                    double grade = Double.parseDouble(sc.nextLine());
                    students.add(new Student(name, grade));
                    System.out.println("Student added.");
                    break;

                case "2":
                    if (students.isEmpty()) {
                        System.out.println("No students available.");
                    }
                    for (Student s : students) {
                        System.out.println(s.name + ": " + s.grade);
                    }
                    break;

                case "3":
                    if (!students.isEmpty()) {
                        double sum = 0;
                        for (Student s : students) sum += s.grade;
                        System.out.println("Class Average: " + sum / students.size());
                    } else {
                        System.out.println("No grades to calculate.");
                    }
                    break;

                case "4":
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
