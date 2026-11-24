import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

REQUIRED_FIELDS = ["userId", "id", "title", "body"]


def validate_api_data(data):
    print("\nAPI DATA VALIDATION")
    print("===================")

    for field in REQUIRED_FIELDS:
        if field in data and data[field] is not None:
            print("PASS:", field, "exists")
        else:
            print("FAIL:", field, "is missing")


def main():
    try:
        response = requests.get(API_URL, timeout=10)

        print("HTTP Status:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            validate_api_data(data)
        else:
            print("API request failed")

    except requests.exceptions.RequestException as error:
        print("API Error:", error)


if __name__ == "__main__":
    main()
