import java.io.*;
import java.net.*;
import org.json.JSONObject;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter city: ");
        String city = sc.nextLine();
        String urlStr = "http://wttr.in/" + city + "?format=j1";
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection)url.openConnection();
        conn.setRequestMethod("GET");
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        StringBuilder sb = new StringBuilder(); String line;
        while((line=br.readLine())!=null) sb.append(line);
        br.close();

        JSONObject obj = new JSONObject(sb.toString());
        JSONObject current = obj.getJSONArray("current_condition").getJSONObject(0);
        System.out.println("Temperature: " + current.getString("temp_C")+"°C");
        System.out.println("Humidity: " + current.getString("humidity")+"%");
        System.out.println("Wind: " + current.getString("windspeedKmph")+" km/h");
    }
}
