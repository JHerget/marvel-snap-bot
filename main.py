from http_util import HttpClient
import json

with open("config.json", "r") as file:
    config = json.loads(file.read())

test = HttpClient.get("https://google.com")
print(test.status_code)
