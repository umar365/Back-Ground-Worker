import requests
import time

# URL of your website
url = "https://sabits-website.onrender.com"  # Replace with your website URL

# Time interval in seconds
interval = 60  # Adjust as needed (e.g., 300 seconds = 5 minutes)

try:
    while True:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Print the response status code
        print(f"Pinged {url}, Status Code: {response.status_code}")
        
        # Wait for the specified interval before the next request
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nStopping the script...")