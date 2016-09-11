# hello-jarod
My code-2040 Fellows Application

import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.json.JSONException;
import org.json.JSONObject;

public class Main {

	private static String token;
	
	public Main()
	{
		token = "66d5f9f688c97246594893b381490a59";
	}
	
	public static void main(String[] args)
	{
		JSONObject json = new JSONObject();
		try {
			json.put(token, "https://github.com/jdrobinson707/hello-jarod");    
		} catch (JSONException e) {}

		CloseableHttpClient httpClient = HttpClientBuilder.create().build();

		try {
			HttpPost request = new HttpPost("http://challenge.code2040.org/api/register");
			StringEntity params = new StringEntity(json.toString());
			request.addHeader("content-type", "application/json");
			request.setEntity(params);
			httpClient.execute(request);

		} catch (Exception ex) {} 
	}
}
