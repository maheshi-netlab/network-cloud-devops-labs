import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(API_URL, timeout=10)

    print("HTTP Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Server:", response.headers.get("Server"))
    print("Response Date:", response.headers.get("Date"))
    print("Content Length:", response.headers.get("Content-Length"))

except requests.exceptions.RequestException as error:
    print("API Error:", error)
