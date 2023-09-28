import requests


def fetch_random_dog_image():
    url = "https://api.thedogapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['url']
    return None


if __name__ == "__main__":
    dog_image_url = fetch_random_dog_image()
    if dog_image_url:
        print(f"Random Dog Image URL: {dog_image_url}")
    else:
        print("Failed to fetch dog image.")
