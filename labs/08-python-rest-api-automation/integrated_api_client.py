import os
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def get_api_token():
    return os.getenv("FIREWALL_API_TOKEN")


def fetch_api_data():
    token = get_api_token()

    if not token:
        print("ERROR: API token is missing")
        return None

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + token
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            timeout=10
        )

        print("HTTP Status:", response.status_code)

        if response.status_code == 200:
            return response.json()

        print("ERROR: API request failed")
        return None

    except requests.exceptions.RequestException as error:
        print("API Error:", error)
        return None


def main():
    data = fetch_api_data()

    if data:
        print("\nAPI RESPONSE")
        print("Post ID:", data["id"])
        print("User ID:", data["userId"])
        print("Title:", data["title"])


if __name__ == "__main__":
    main()
