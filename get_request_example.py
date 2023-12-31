import requests

# Define the URL
url = "http://127.0.0.1:8000/api/basic_info/"

# Make the GET request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    print("Request successful!")
    # Print the response content
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
