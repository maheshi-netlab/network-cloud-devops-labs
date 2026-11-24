import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "Accept": "application/json",
    "User-Agent": "Network-Security-Automation/1.0"
}

try:
    response = requests.get(
        API_URL,
        headers=headers,
        timeout=10
    )

    print("HTTP Status:", response.status_code)
    print("Request Headers:")

    for key, value in response.request.headers.items():
        print(key + ":", value)

    print("\nResponse Content-Type:")
    print(response.headers.get("Content-Type"))

except requests.exceptions.RequestException as error:
    print("API Error:", error)
