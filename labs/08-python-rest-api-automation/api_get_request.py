import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(API_URL, timeout=10)

    print("====================================")
    print(" REST API GET REQUEST")
    print("====================================")

    print("HTTP Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("API Request Successful")
        print("Post ID:", data["id"])
        print("User ID:", data["userId"])
        print("Title:", data["title"])
        print("Body:", data["body"])
    else:
        print("API Request Failed")

except requests.exceptions.Timeout:
    print("ERROR: API request timed out")

except requests.exceptions.RequestException as error:
    print("ERROR:", error)

