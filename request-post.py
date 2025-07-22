import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Hello API",
    "body": "Practicing POST requests in Python",
    "userId": 10
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    returned_data = response.json()
    print("POST Request Successful. Returned Data:")
    print(returned_data)
else:
    print("POST Request Failed:", response.status_code)
