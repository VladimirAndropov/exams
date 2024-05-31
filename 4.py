import sys
import requests

def http_client(url):
    try:
        response = requests.get(url)
        print(response.text)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        http_client(sys.argv[1])
    else:
        print("Please provide a URL as argument.")
