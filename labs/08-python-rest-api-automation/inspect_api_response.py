import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(API_URL, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("JSON RESPONSE STRUCTURE")
        print("=======================")

        print(json.dumps(data, indent=4))

        print("\nDATA TYPE:", type(data).__name__)

        for key, value in data.items():
            print(key, "=", value, "| Type:", type(value).__name__)

    else:
        print("API request failed:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API Error:", error)
