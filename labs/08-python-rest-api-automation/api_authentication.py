import os
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

API_TOKEN = os.getenv("FIREWALL_API_TOKEN")

if not API_TOKEN:
    print("ERROR: API token is not configured")
    exit(1)

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + API_TOKEN
}

try:
    response = requests.get(
        API_URL,
        headers=headers,
        timeout=10
    )

    print("HTTP Status:", response.status_code)
    print("Authorization Header: Bearer <REDACTED>")

    if response.status_code == 200:
        print("API request successful")
    else:
        print("API request returned an error")

except requests.exceptions.RequestException as error:
    print("API Error:", error)
