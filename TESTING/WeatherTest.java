import java.net.*;
import java.io.*;

public class WeatherTest {
	public static void main(String[] args) throws Exception {
		System.out.println("Hello,");
		URL localhost = new URL("https://api.openweathermap.org/data/2.5/weather?id=5375916&appid=92dcc5b18216a951232bc612e25104e0&units=imperial");
		URLConnection lc = localhost.openConnection();
		BufferedReader in = new BufferedReader(
				new InputStreamReader(
					lc.getInputStream()));
		String inputLine;

		while ((inputLine = in.readLine()) != null)
			System.out.println(inputLine);
		in.close();
	}
}
