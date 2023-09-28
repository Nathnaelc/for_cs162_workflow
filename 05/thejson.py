import requests

response = requests.get("https://httpbin.org/json")
data = response.json()

print(f"Request:\nGET {response.url}\n")
print(
    f"Response:\nStatus Code: {response.status_code}\nContent Type: {response.headers['content-type']}\nJSON Response: {data}")
5
