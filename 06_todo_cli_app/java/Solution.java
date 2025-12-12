import java.util.*;
import java.io.*;
import org.json.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String file = "tasks.json";
        JSONArray tasks = new JSONArray();
        if(new File(file).exists()) tasks = new JSONArray(new String(java.nio.file.Files.readAllBytes(new File(file).toPath())));

        while(true){
            System.out.println("\n1.Add 2.Remove 3.Complete 4.Show 5.Exit");
            String choice = sc.next();
            sc.nextLine();
            if(choice.equals("1")){
                System.out.print("Enter task: "); String task = sc.nextLine();
                JSONObject obj = new JSONObject(); obj.put("task",task); obj.put("done",false);
                tasks.put(obj);
            } else if(choice.equals("2")){
                System.out.print("Index to remove: "); int idx=sc.nextInt();
                tasks.remove(idx);
            } else if(choice.equals("3")){
                System.out.print("Index to complete: "); int idx=sc.nextInt();
                tasks.getJSONObject(idx).put("done",true);
            } else if(choice.equals("4")){
                for(int i=0;i<tasks.length();i++){
                    JSONObject t=tasks.getJSONObject(i);
                    System.out.println(i+": "+t.getString("task")+" ["+(t.getBoolean("done")?"Done":"Pending")+"]");
                }
            } else break;
        }
        try(PrintWriter pw=new PrintWriter(file)){pw.print(tasks.toString());}
        System.out.println("Tasks saved!");
    }
}
