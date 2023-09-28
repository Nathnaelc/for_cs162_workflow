import requests

response = requests.get("https://httpbin.org/image/jpeg")
with open("image.jpeg", "wb") as file:
    file.write(response.content)

print(f"Request:\nGET {response.url}\n")
print(
    f"Response:\nStatus Code: {response.status_code}\nContent Type: {response.headers['content-type']}\nSaved as: image.jpeg")
