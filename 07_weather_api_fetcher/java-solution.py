import java.net.*;
import java.io.*;
import org.json.*;

public class WeatherFetcher {
    public static void main(String[] args) throws Exception {

        String apiKey = "YOUR_API_KEY";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter city name: ");
        String city = br.readLine();

        String urlStr =
            "https://api.openweathermap.org/data/2.5/weather?q=" +
            city + "&appid=" + apiKey + "&units=metric";

        URL url = new URL(urlStr);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));

        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject obj = new JSONObject(response.toString());
        double temp = obj.getJSONObject("main").getDouble("temp");
        String desc = obj.getJSONArray("weather")
                         .getJSONObject(0)
                         .getString("description");

        System.out.println("Temperature: " + temp + "°C");
        System.out.println("Weather: " + desc);
    }
}
