import java.io.*;
import java.net.*;
import org.json.JSONObject;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Amount: "); double amt = sc.nextDouble();
        System.out.print("From (USD/EUR/INR/...): "); String from = sc.next().toUpperCase();
        System.out.print("To (USD/EUR/INR/...): "); String to = sc.next().toUpperCase();

        String urlStr = "https://api.exchangerate.host/convert?from="+from+"&to="+to;
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection)url.openConnection();
        conn.setRequestMethod("GET");
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        StringBuilder sb = new StringBuilder(); String line;
        while((line = br.readLine())!=null) sb.append(line);
        br.close();

        JSONObject obj = new JSONObject(sb.toString());
        double rate = obj.getJSONObject("info").getDouble("rate");
        System.out.printf("%.2f %s = %.2f %s%n", amt, from, amt*rate, to);
    }
}

