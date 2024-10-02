import requests
import time

def keep_alive(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        time.sleep(60)  # Wait for 60 seconds before the next request

if __name__ == "__main__":
    target_url = "https://sabits-website.onrender.com"  # Change this to your website
    keep_alive(target_url)
