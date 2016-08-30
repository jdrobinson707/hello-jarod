# hello-jarod
My code-2040 Fellows Application

import json

string url = 66d5f9f688c97246594893b381490a59;
Dictionary<token, github> points = new Dictionary<token, github>
{
  { url, "https://github.com/jdrobinson707/hello-jarod" };
}
string json = JsonConvert.SerializeObject(url, Formatting.Indented);
Console.WriteLine(json);
