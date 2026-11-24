import requests

API_URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/9999"
]

def check_api_status(url):
    try:
        response = requests.get(url, timeout=10)

        print("\nAPI URL:", url)
        print("HTTP Status:", response.status_code)

        if response.status_code == 200:
            print("SUCCESS: API request completed")

        elif response.status_code == 401:
            print("ERROR: Authentication required")

        elif response.status_code == 403:
            print("ERROR: Access forbidden")

        elif response.status_code == 404:
            print("ERROR: API resource not found")

        elif response.status_code == 429:
            print("WARNING: API rate limit exceeded")

        elif response.status_code >= 500:
            print("ERROR: Server-side failure")

        else:
            print("WARNING: Unexpected HTTP response")

    except requests.exceptions.Timeout:
        print("ERROR: API request timed out")

    except requests.exceptions.RequestException as error:
        print("ERROR:", error)


def main():
    for url in API_URLS:
        check_api_status(url)


if __name__ == "__main__":
    main()
